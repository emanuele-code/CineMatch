from flask import Blueprint, jsonify, render_template, request, session
from bson import ObjectId
from pymongo import MongoClient

movie_card_bp = Blueprint('movie_card', __name__)

# fetch a movie from the collection by id
def get_film_by_id(film_id):
    db = movie_card_bp.mongo.db
    film = db.films.find_one({'id': film_id})
    if film:
        film['_id'] = str(film['_id'])  # convert ObjectId to string
    return film

# fetch recommended movies of the same genre, excluding the current one
def get_film_consigliati(film):
    db = movie_card_bp.mongo.db
    consigliati = list(db.films.find({
        'genere': film['genere'],
        'id': {'$ne': film['id']}
    }))
    for f in consigliati:
        f['_id'] = str(f['_id'])
    return consigliati

# user information for the movie: rating, status, review
def get_info_utente_per_film(film_oid):
    db = movie_card_bp.mongo.db
    id_utente = session.get('id_utente')
    utente = db.utenti.find_one({"_id": ObjectId(id_utente)}) if id_utente else None

    voto = None
    stato = None
    username = None
    recensione = ""

    # check if the user has already added info about this movie
    if utente:
        username = utente.get('username')
        for fv in utente.get('filmVisti', []):
            if str(fv['film_id']) == str(film_oid):
                voto = fv.get('voto')
                stato = fv.get('stato')
                recensione = fv.get('recensione', "")
                break

    return voto, stato, username, recensione

# all public user reviews for a movie
def get_recensioni_pubbliche(film_oid):
    db = movie_card_bp.mongo.db
    recensioni = []

    utenti_con_recensioni = db.utenti.find({
        "filmVisti": {
            "$elemMatch": {
                "film_id": ObjectId(film_oid),
                "recensione": {"$ne": ""}
            }
        }
    })

    # for each user with a review, add username and text
    for utente in utenti_con_recensioni:
        for f in utente['filmVisti']:
            if str(f['film_id']) == str(film_oid) and f.get('recensione'):
                recensioni.append({
                    "nome_utente": utente['username'],
                    "testo": f['recensione']
                })

    return recensioni

# route to display the movie card
@movie_card_bp.route('/movie-card/<int:film_id>')
def movie_card(film_id):
    film = get_film_by_id(film_id)
    if not film:
        return "Film not found", 404

    consigliati = get_film_consigliati(film)
    recensioni = get_recensioni_pubbliche(film['_id'])

    utente_loggato = 'id_utente' in session
    voto_utente, stato_utente, username, recensione_utente = \
        get_info_utente_per_film(film['_id'])

    return render_template(
        'movie-card.html',
        film=film,
        consigliati=consigliati,
        utente_loggato=utente_loggato,
        voto_utente=voto_utente,
        stato_utente=stato_utente,
        username=username,
        recensione_utente=recensione_utente,
        recensioni=recensioni
    )

# route to save or update a user's review
@movie_card_bp.route('/movie-card/<film_id>', methods=['POST'])
def salva_recensione(film_id):
    db = movie_card_bp.mongo.db
    nuovo_testo = request.form.get('recensione', '').strip()
    id_utente = session.get('id_utente')

    if not id_utente:
        return jsonify({"error": "User not authenticated"}), 401

    utente = db.utenti.find_one({"_id": ObjectId(id_utente)})
    if not utente:
        return jsonify({"error": "User not found"}), 404

    # update review if the movie is already in 'filmVisti'
    trovato = False
    for fv in utente.get('filmVisti', []):
        if str(fv['film_id']) == film_id:
            fv['recensione'] = nuovo_testo
            trovato = True
            break

    # if movie not present, add new entry
    if not trovato:
        utente.setdefault('filmVisti', []).append({
            "film_id": ObjectId(film_id),
            "recensione": nuovo_testo
        })

    # update user document in db
    db.utenti.update_one(
        {"_id": ObjectId(id_utente)},
        {"$set": {"filmVisti": utente['filmVisti']}}
    )

    return jsonify({"success": True})
