from flask import Blueprint, request, jsonify, session, render_template
from bson import ObjectId
from pymongo import MongoClient

recensioni_bp = Blueprint('recensioni', __name__)

client = MongoClient()
db = client.cinematch
utenti = db.utenti

@recensioni_bp.route('/film/<film_id>', methods=['GET'])
def film_detail(film_id):
    film_oid = ObjectId(film_id)
    print(film_oid)

    # Qui recuperi i dati del film dal db (esempio, adattalo alla tua struttura)
    film = db.films.find_one({'_id': film_oid})
    if not film:
        return "Film non trovato", 404

    # Recupera tutte le recensioni del film dagli utenti
    pipeline = [
        {"$unwind": "$filmVisti"},
        {"$match": {"filmVisti.film_id": film_oid, "filmVisti.recensione": {"$ne": ""}}},
        {"$project": {
            "nome_utente": "$username",
            "testo": "$filmVisti.recensione"
        }}
    ]
    recensioni_cursor = utenti.aggregate(pipeline)
    recensioni = list(recensioni_cursor)

    # Passa anche altre info necessarie al template, ad esempio consigliati, stato utente ecc.
    consigliati = []  # Implementa la logica per i consigliati
    username = session.get('username')
    utente_loggato = bool(username)

    # Esempio di stato_utente e voto_utente se loggato (da personalizzare)
    stato_utente = None
    voto_utente = 0
    if utente_loggato:
        utente = utenti.find_one({"username": username})
        for fv in utente.get("filmVisti", []):
            if fv["film_id"] == film_oid:
                stato_utente = fv.get("stato", None)
                voto_utente = fv.get("voto", 0)
                break

    return render_template('film_detail.html',
                           film=film,
                           recensioni=recensioni,
                           consigliati=consigliati,
                           username=username,
                           utente_loggato=utente_loggato,
                           stato_utente=stato_utente,
                           voto_utente=voto_utente)
