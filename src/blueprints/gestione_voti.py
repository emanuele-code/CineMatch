from flask   import Blueprint, request, jsonify, session
from bson    import ObjectId
from pymongo import MongoClient

voti_bp = Blueprint('voti_bp', __name__)

# update the rating of a movie for the user in session
@voti_bp.route('/aggiorna_voto', methods=['POST'])
def aggiorna_voto():
    user_id = session['id_utente']

    # data sent via JSON
    data     = request.json
    film_id  = data.get('film_id')  # id of the movie to rate
    voto     = data.get('voto')     # user's rating (1-5)

    # update the rating in the user's filmVisti list
    voti_bp.mongo.db.utenti.update_one(
        {
            '_id': ObjectId(user_id),
            'filmVisti.film_id': ObjectId(film_id)
        },
        {
            '$set': {'filmVisti.$.voto': voto}  # update the vote field
        }
    )

    # return confirmation with updated rating
    return jsonify({'success': True, 'voto': voto})
