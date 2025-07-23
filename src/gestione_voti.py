from flask   import Blueprint, request, jsonify, session
from bson    import ObjectId
from pymongo import MongoClient


voti_bp = Blueprint('voti_bp', __name__)

client = MongoClient()
db     = client.cinematch
utenti = db.utenti  



# Define a route to handle vote updates for a film
@voti_bp.route('/aggiorna_voto', methods=['POST'])
def aggiorna_voto():
    if 'id_utente' not in session:
        return jsonify({'error': 'Non autenticato'}), 401
    user_id = session['id_utente']

    # Get the JSON data from the request
    data    = request.json
    film_id = data.get('film_id')  # ID of the film to be rated
    voto    = data.get('voto')     # User's vote (should be between 1 and 5)

    # Validate the input data
    if not film_id or not voto or not (1 <= voto <= 5):
        return jsonify({'error': 'Dati non validi'}), 400

    # Try to update the vote for the given film in the user's "filmVisti" list
    result = utenti.update_one(
        {
            '_id': ObjectId(user_id),                    
            'filmVisti.film_id': ObjectId(film_id)        
        },
        {
            '$set': {'filmVisti.$.voto': voto}            # Update the "voto" field of the matched film
        }
    )

    # Return a success response with the updated vote
    return jsonify({'success': True, 'voto': voto})

