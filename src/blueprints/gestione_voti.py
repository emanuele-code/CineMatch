from flask   import Blueprint, request, jsonify, session
from bson    import ObjectId
from pymongo import MongoClient

voti_bp = Blueprint('voti_bp', __name__)

# aggiorna il voto di un film per l'utente in sessione
@voti_bp.route('/aggiorna_voto', methods=['POST'])
def aggiorna_voto():
    user_id = session['id_utente']

    # dati inviati via JSON
    data    = request.json
    film_id = data.get('film_id')  # id del film da votare
    voto    = data.get('voto')     # voto dell'utente (1-5)

    # aggiorna il voto nella lista filmVisti dell'utente
    voti_bp.mongo.db.utenti.update_one(
        {
            '_id': ObjectId(user_id),
            'filmVisti.film_id': ObjectId(film_id)
        },
        {
            '$set': {'filmVisti.$.voto': voto}  # aggiorna il campo voto
        }
    )

    # restituisce conferma con il voto aggiornato
    return jsonify({'success': True, 'voto': voto})
