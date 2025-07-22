from flask import Blueprint, request, jsonify, session
from bson import ObjectId
from pymongo import MongoClient

stati_bp = Blueprint('stati', __name__)

client = MongoClient()
db     = client.cinematch
utenti = db.utenti


def aggiungi_film(result, user_oid, film_oid, stato):
    # Se il film non esiste ancora, lo aggiunge
    if result.matched_count == 0:
        utenti.update_one(
            {'_id': user_oid},
            {'$push': {'filmVisti': {
                'film_id': film_oid,
                'voto': 0,
                'stato': stato
            }}}
        )


@stati_bp.route('/aggiorna_stato', methods=['POST'])
def aggiorna_stato():
    if 'id_utente' not in session:
        return jsonify({'error': 'Non autenticato'}), 401

    user_id = session['id_utente']
    data = request.json
    film_id = data.get('film_id')
    stato = data.get('stato')  # può essere 'visto', 'da vedere' o None

    if not film_id:
        return jsonify({'error': 'film_id mancante'}), 400

    film_oid = ObjectId(film_id)
    user_oid = ObjectId(user_id)


    # Rimuovi lo stato se stato è null/None
    if stato == 'nessuno':
        utenti.update_one(
            {'_id': user_oid},
            {'$pull': {'filmVisti': {'film_id': film_oid}}}
        )
    elif stato == 'da vedere':
        result = utenti.update_one(
            {'_id': user_oid, 'filmVisti.film_id': film_oid},
            {
                '$set': {
                    'filmVisti.$.stato': stato,
                    'filmVisti.$.voto': 0
                }
            }
        )
        aggiungi_film(result, user_oid, film_oid, stato)
    else:
        # Aggiorna stato se il film esiste già
        result = utenti.update_one(
            {'_id': user_oid, 'filmVisti.film_id': film_oid},
            {'$set': {'filmVisti.$.stato': stato}}
        )
        aggiungi_film(result, user_oid, film_oid, stato)

        

    return jsonify({'success': True, 'stato': stato})
