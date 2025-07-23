from flask import Blueprint, request, jsonify, session
from bson import ObjectId
from pymongo import MongoClient

stati_bp = Blueprint('stati_bp', __name__)

client = MongoClient()
db     = client.cinematch
utenti = db.utenti


def aggiungi_film(result, user_oid, film_oid, stato):
    # if the film doesn´t exist is added
    if result.matched_count == 0:
        utenti.update_one(
            {'_id': user_oid},
            {'$push': {'filmVisti': {
                'film_id': film_oid,
                'voto'   : 0,
                'stato'  : stato
            }}}
        )



# Route to update the viewing status of a film for the current user
@stati_bp.route('/aggiorna_stato', methods=['POST'])
def aggiorna_stato():
    if 'id_utente' not in session:
        return jsonify({'error': 'Non autenticato'}), 401

    user_id = session['id_utente']

    # Parse JSON data from the request
    data    = request.json
    film_id = data.get('film_id')
    stato   = data.get('stato')  # expected values: 'visto', 'da vedere' o 'nessuno'

    # If no film_id is provided, return an error
    if not film_id:
        return jsonify({'error': 'film_id mancante'}), 400

    # Convert string IDs to ObjectId for MongoDB querying
    film_oid = ObjectId(film_id)
    user_oid = ObjectId(user_id)


    # If status is "nessuno", remove the film from the user's list
    if stato == 'nessuno':
        utenti.update_one(
            {'_id': user_oid},
            {'$pull': {'filmVisti': {'film_id': film_oid}}}
        )
    # If status is "da vedere", either update or add the film with initial vote = 0
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
        # If the update didn't match any document, add the film to the list
        aggiungi_film(result, user_oid, film_oid, stato)
    else:
        # For other valid statuses (e.g. 'visto'), try to update the film status
        result = utenti.update_one(
            {'_id': user_oid, 'filmVisti.film_id': film_oid},
            {'$set': {'filmVisti.$.stato': stato}}
        )
        # If the update didn't find the film, add it
        aggiungi_film(result, user_oid, film_oid, stato)

        
    # Return success response with the new status
    return jsonify({'success': True, 'stato': stato})
