from flask import Blueprint, request, jsonify, session
from bson import ObjectId

stati_bp = Blueprint('stati_bp', __name__)

# add a movie to the user's list if it doesn't exist
def aggiungi_film(risultato, utente_oid, film_oid, stato):
    if risultato.matched_count == 0:
        stati_bp.mongo.db.utenti.update_one(
            {'_id': utente_oid},
            {'$push': {'filmVisti': {
                'film_id': film_oid,
                'voto'   : 0,       # initial rating
                'stato'  : stato
            }}}
        )

# update the status of a movie for the user in session
@stati_bp.route('/aggiorna_stato', methods=['POST'])
def aggiorna_stato():
    id_utente = session['id_utente']

    # data sent via JSON
    data = request.json
    film_id = data.get('film_id')
    stato = data.get('stato')  # expected values: 'visto', 'da vedere', 'nessuno'

    # convert to ObjectId for MongoDB
    film_oid = ObjectId(film_id)
    utente_oid = ObjectId(id_utente)

    if stato == 'nessuno':
        # remove the movie from the list if status is "none"
        stati_bp.mongo.db.utenti.update_one(
            {'_id': utente_oid},
            {'$pull': {'filmVisti': {'film_id': film_oid}}}
        )
    elif stato == 'da vedere':
        # update or add the movie with initial rating = 0
        risultato = stati_bp.mongo.db.utenti.update_one(
            {'_id': utente_oid, 'filmVisti.film_id': film_oid},
            {'$set': {'filmVisti.$.stato': stato, 'filmVisti.$.voto': 0}}
        )
        aggiungi_film(risultato, utente_oid, film_oid, stato)
    else:
        # for other valid states (e.g., 'visto') attempt to update
        risultato = stati_bp.mongo.db.utenti.update_one(
            {'_id': utente_oid, 'filmVisti.film_id': film_oid},
            {'$set': {'filmVisti.$.stato': stato}}
        )
        aggiungi_film(risultato, utente_oid, film_oid, stato)

    # response with updated status
    return jsonify({'success': True, 'stato': stato})
