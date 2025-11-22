from flask import Blueprint, jsonify, render_template, request, session
from bson import ObjectId
from pymongo import MongoClient

movie_card_bp = Blueprint('movie_card', __name__)

# prende un film dalla collezione tramite id
def get_film_by_id(film_id):
    db = movie_card_bp.mongo.db
    film = db.films.find_one({'id': film_id})
    if film:
        film['_id'] = str(film['_id'])  # converte ObjectId in stringa
    return film

# prende film consigliati dello stesso genere, escluso quello attuale
def get_film_consigliati(film):
    db = movie_card_bp.mongo.db
    consigliati = list(db.films.find({
        'genere': film['genere'],
        'id': {'$ne': film['id']}
    }))
    for f in consigliati:
        f['_id'] = str(f['_id'])
    return consigliati

# informazioni dell'utente sul film: voto, stato, recensione
def get_info_utente_per_film(film_oid):
    db = movie_card_bp.mongo.db
    id_utente = session.get('id_utente')
    utente = db.utenti.find_one({"_id": ObjectId(id_utente)}) if id_utente else None

    voto = None
    stato = None
    username = None
    recensione = ""

    # cerca se l'utente ha già aggiunto info su questo film
    if utente:
        username = utente.get('username')
        for fv in utente.get('filmVisti', []):
            if str(fv['film_id']) == str(film_oid):
                voto = fv.get('voto')
                stato = fv.get('stato')
                recensione = fv.get('recensione', "")
                break

    return voto, stato, username, recensione

# tutte le recensioni pubbliche degli utenti su un film
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

    # per ogni utente con recensione, aggiungi nome e testo
    for utente in utenti_con_recensioni:
        for f in utente['filmVisti']:
            if str(f['film_id']) == str(film_oid) and f.get('recensione'):
                recensioni.append({
                    "nome_utente": utente['username'],
                    "testo": f['recensione']
                })

    return recensioni

# route per visualizzare la scheda del film
@movie_card_bp.route('/movie-card/<int:film_id>')
def movie_card(film_id):
    film = get_film_by_id(film_id)
    if not film:
        return "Film non trovato", 404

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

# route per salvare o aggiornare una recensione dell'utente
@movie_card_bp.route('/movie-card/<film_id>', methods=['POST'])
def salva_recensione(film_id):
    db = movie_card_bp.mongo.db
    nuovo_testo = request.form.get('recensione', '').strip()
    id_utente = session.get('id_utente')

    if not id_utente:
        return jsonify({"error": "Utente non autenticato"}), 401

    utente = db.utenti.find_one({"_id": ObjectId(id_utente)})
    if not utente:
        return jsonify({"error": "Utente non trovato"}), 404

    # aggiorna recensione se film già presente in 'filmVisti'
    trovato = False
    for fv in utente.get('filmVisti', []):
        if str(fv['film_id']) == film_id:
            fv['recensione'] = nuovo_testo
            trovato = True
            break

    # se film non presente, aggiungi nuovo elemento
    if not trovato:
        utente.setdefault('filmVisti', []).append({
            "film_id": ObjectId(film_id),
            "recensione": nuovo_testo
        })

    # aggiorna il documento utente nel db
    db.utenti.update_one(
        {"_id": ObjectId(id_utente)},
        {"$set": {"filmVisti": utente['filmVisti']}}
    )

    return jsonify({"success": True})
