from flask import Blueprint, request, jsonify, session
from bson import ObjectId
from pymongo import MongoClient

voti_bp = Blueprint('voti', __name__)

client = MongoClient()  # Assicurati che la connessione sia configurata correttamente
db = client.cinematch
utenti = db.utenti

@voti_bp.route('/aggiorna_voto', methods=['POST'])
def aggiorna_voto():
    if 'id_utente' not in session:
        return jsonify({'error': 'Non autenticato'}), 401

    user_id = session['id_utente']
    data = request.json
    film_id = data.get('film_id')
    voto = data.get('voto')

    if not film_id or not voto or not (1 <= voto <= 5):
        return jsonify({'error': 'Dati non validi'}), 400

    # Aggiorna il voto nel filmVisti per questo utente e film
    result = utenti.update_one(
        {
            '_id': ObjectId(user_id),
            'filmVisti.film_id': ObjectId(film_id)
        },
        {
            '$set': {'filmVisti.$.voto': voto}
        }
    )

    return jsonify({'success': True, 'voto': voto})
