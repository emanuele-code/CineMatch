from flask import Blueprint, request, jsonify, session
from bson import ObjectId

stati_bp = Blueprint('stati_bp', __name__)

# aggiunge un film alla lista dell'utente se non esiste
def aggiungi_film(risultato, utente_oid, film_oid, stato):
    if risultato.matched_count == 0:
        stati_bp.mongo.db.utenti.update_one(
            {'_id': utente_oid},
            {'$push': {'filmVisti': {
                'film_id': film_oid,
                'voto'   : 0,       # voto iniziale
                'stato'  : stato
            }}}
        )

# aggiorna lo stato di un film per l'utente in sessione
@stati_bp.route('/aggiorna_stato', methods=['POST'])
def aggiorna_stato():
    id_utente = session['id_utente']

    # dati inviati via JSON
    data = request.json
    film_id = data.get('film_id')
    stato = data.get('stato')  # valori attesi: 'visto', 'da vedere', 'nessuno'

    # converte in ObjectId per MongoDB
    film_oid = ObjectId(film_id)
    utente_oid = ObjectId(id_utente)

    if stato == 'nessuno':
        # rimuove il film dalla lista se lo stato è "nessuno"
        stati_bp.mongo.db.utenti.update_one(
            {'_id': utente_oid},
            {'$pull': {'filmVisti': {'film_id': film_oid}}}
        )
    elif stato == 'da vedere':
        # aggiorna o aggiunge il film con voto iniziale = 0
        risultato = stati_bp.mongo.db.utenti.update_one(
            {'_id': utente_oid, 'filmVisti.film_id': film_oid},
            {'$set': {'filmVisti.$.stato': stato, 'filmVisti.$.voto': 0}}
        )
        aggiungi_film(risultato, utente_oid, film_oid, stato)
    else:
        # per altri stati validi (es. 'visto') prova ad aggiornare
        risultato = stati_bp.mongo.db.utenti.update_one(
            {'_id': utente_oid, 'filmVisti.film_id': film_oid},
            {'$set': {'filmVisti.$.stato': stato}}
        )
        aggiungi_film(risultato, utente_oid, film_oid, stato)

    # risposta con stato aggiornato
    return jsonify({'success': True, 'stato': stato})
