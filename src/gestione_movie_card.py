from flask import Blueprint, jsonify, render_template, request, session
from bson import ObjectId
from pymongo import MongoClient

movie_card_bp = Blueprint('movie_card', __name__)

client = MongoClient()
db     = client.cinematch
films  = db.films
utenti = db.utenti


# get film in the collections by its id
def get_film_by_id(film_id):
    film = films.find_one({'id': film_id})
    if film:
        film['_id'] = str(film['_id'])
    return film


# get a list of suggested films based on the same genre of the film
def get_film_consigliati(film):
    consigliati = list(films.find({'genere': film['genere'], 'id': {'$ne': film['id']}}))
    for f in consigliati:
        f['_id'] = str(f['_id'])
    return consigliati


# get films detail added by the user as the review, status and score
def get_info_utente_per_film(film_oid):
    id_utente = session.get('id_utente')
    utente    = utenti.find_one({"_id": ObjectId(id_utente)}) if id_utente else None

    voto       = None
    stato      = None
    username   = None
    recensione = ""

    # retrieve information inserted by the session user about the film selected
    if utente:
        username = utente.get('username')
        for fv in utente.get('filmVisti', []):
            if str(fv['film_id']) == str(film_oid):
                voto       = fv.get('voto')
                stato      = fv.get('stato')
                recensione = fv.get('recensione', "")
                break

    return voto, stato, username, recensione



# retrieve all reviews inserted by users
def get_recensioni_pubbliche(film_oid):
    recensioni = []
    utenti_con_recensioni = utenti.find({
        "filmVisti": {
            "$elemMatch": {
                "film_id"   : ObjectId(film_oid),
                "recensione": {"$ne": ""}
            }
        }
    })

    # look for user who inserted a review and fill an array with those information
    for utente in utenti_con_recensioni:
        for f in utente['filmVisti']:
            if str(f['film_id']) == str(film_oid) and f.get('recensione'):
                recensioni.append({
                    "nome_utente" : utente['username'],
                    "testo"       : f['recensione']
                })

    return recensioni


@movie_card_bp.route('/movie-card/<int:film_id>')
def movie_card(film_id):
    film = get_film_by_id(film_id)
    if not film:
        return "Film non trovato", 404

    consigliati = get_film_consigliati(film)
    recensioni  = get_recensioni_pubbliche(film['_id'])

    utente_loggato = 'id_utente' in session
    voto_utente, stato_utente, username, recensione_utente = get_info_utente_per_film(film['_id'])

    return render_template('movie-card.html',
                           film=film,
                           consigliati=consigliati,
                           utente_loggato=utente_loggato,
                           voto_utente=voto_utente,
                           stato_utente=stato_utente,
                           username=username,
                           recensione_utente=recensione_utente,
                           recensioni=recensioni)





# Route to handle saving or updating a user's review for a specific movie (by film_id)
@movie_card_bp.route('/movie-card/<film_id>', methods=['POST'])
def salva_recensione(film_id):
    if 'id_utente' not in session:
        return jsonify({"error": "Utente non loggato"}), 401

    # Get the new review text from the form (trim whitespace)
    nuovo_testo = request.form.get('recensione', '').strip()

    id_utente = session['id_utente']

    # Find the user document in the database
    utente = utenti.find_one({"_id": ObjectId(id_utente)})
    if not utente:
        return jsonify({"error": "Utente non trovato"}), 404

    # Try to find the movie in the user's 'filmVisti' list
    trovato = False
    for fv in utente.get('filmVisti', []):
        if str(fv['film_id']) == film_id:
            fv['recensione'] = nuovo_testo
            trovato = True
            break

    # If the movie is not found in 'filmVisti', add it with the new review
    if not trovato:
        utente.setdefault('filmVisti', []).append({
            "film_id": ObjectId(film_id),
            "recensione": nuovo_testo
        })

    # Update the user's document in the database with the new or modified 'filmVisti' list
    utenti.update_one(
        {"_id": ObjectId(id_utente)},
        {"$set": {"filmVisti": utente['filmVisti']}}
    )
    
    # Return a success response in JSON format
    return jsonify({"success": True})