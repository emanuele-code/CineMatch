from flask import Flask, render_template, session, redirect, url_for, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from src.registrazione import registrazione_bp  # import blueprint
from src.login import login_bp
from flask_login import login_required

app = Flask(__name__)
app.secret_key = 'key'  # serve a flask per gestire la sessione

# Configura la connessione a MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/cinematch"

# Inizializza Flask-PyMongo
mongo = PyMongo(app)

# Passo la connessione mongo al blueprint così può usarla
registrazione_bp.mongo = mongo
login_bp.mongo = mongo

# Registra i blueprint
app.register_blueprint(registrazione_bp, url_prefix='/registrazione')
app.register_blueprint(login_bp, url_prefix='/login')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/lista')
def lista():
    film_list = list(mongo.db.films.find())
    for film in film_list:
        film['_id'] = str(film['_id'])
    return render_template('lista.html', film_list=film_list)


@app.route('/movie-card/<int:film_id>')
def movie_card(film_id):
    film = mongo.db.films.find_one({'id': film_id})

    if film is None:
        return "Film non trovato", 404

    film['_id'] = str(film['_id'])
    consigliati = list(mongo.db.films.find({'genere': film['genere'], 'id': {'$ne': film_id}}))
    for consiglio in consigliati:
        consiglio['_id'] = str(consiglio['_id'])

    utente_loggato = 'id_utente' in session
    voto_utente = None
    stato_utente = None

    if utente_loggato:
        id_utente = session.get('id_utente')
        utente = mongo.db.utenti.find_one({"_id": ObjectId(id_utente)})

        if utente and 'filmVisti' in utente:
            # Cerca il film nella lista filmVisti dell'utente
            for film_visto in utente['filmVisti']:
                # film_id è ObjectId, film['_id'] è stringa -> fai confronto coerente
                if str(film_visto['film_id']) == film['_id']:
                    voto_utente = film_visto.get('voto')
                    stato_utente = film_visto.get('stato')
                    break

    return render_template('movie-card.html', film=film, consigliati=consigliati,
                           utente_loggato=utente_loggato,
                           voto_utente=voto_utente,
                           stato_utente=stato_utente)


@app.route('/logged-home-page')
def logged_home_page():
    id_utente = session.get('id_utente')
    if not id_utente:
        return redirect(url_for('login.login'))

    utente = mongo.db.utenti.find_one({"_id": ObjectId(id_utente)})
    film_visti_ids = utente.get('filmVisti', [])

    film_visti = list(mongo.db.films.find({'_id': {'$in': film_visti_ids}}))
    generi_preferiti = list({film['genere'] for film in film_visti})

    consigliati = list(mongo.db.films.aggregate([
        {
            '$match': {
                'genere': {'$in': generi_preferiti},
                '_id': {'$nin': film_visti_ids}
            }
        },
        {'$sample': {'size': 16}}
    ]))

    ultime_uscite = list(mongo.db.films.aggregate([
        {'$match': {'uscita': {'$gte': '2018'}}},
        {'$sample': {'size': 5}}
    ]))

    for film in film_visti + ultime_uscite + consigliati:
        film['_id'] = str(film['_id'])

    return render_template('logged-home-page.html', film_visti=film_visti, ultime_uscite=ultime_uscite, consigliati=consigliati)



@app.route('/modifica-stelle/<film_id>', methods=['POST'])
def modifica_stelle(film_id):
    if 'id_utente' not in session:
        return jsonify(success=False, error='Non autorizzato'), 401

    data = request.get_json()
    nuove_stelle = data.get('stelle')

    if not isinstance(nuove_stelle, int) or not (0 <= nuove_stelle <= 5):
        return jsonify(success=False, error='Valore stelle non valido'), 400

    try:
        oid = ObjectId(film_id)
    except Exception:
        return jsonify(success=False, error='ID film non valido'), 400

    film = mongo.db.films.find_one({'_id': oid})
    if not film:
        return jsonify(success=False, error='Film non trovato'), 404

    mongo.db.films.update_one({'_id': oid}, {'$set': {'stelle': nuove_stelle}})
    return jsonify(success=True)



if __name__ == "__main__":
    app.run(debug=True)
