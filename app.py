from flask import Flask, render_template, session, redirect, url_for, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from src.registrazione import registrazione_bp  # import blueprint
from src.login import login_bp
from src.gestione_voti import voti_bp
from src.gestione_stati import stati_bp
from src.gestione_logged_home_page import logged_home_page_bp

app = Flask(__name__)
app.secret_key = 'key'  # serve a flask per gestire la sessione

# Configura la connessione a MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/cinematch"

# Inizializza Flask-PyMongo
mongo = PyMongo(app)

# Passo la connessione mongo al blueprint così può usarla
registrazione_bp.mongo    = mongo
login_bp.mongo            = mongo
voti_bp.mongo             = mongo
stati_bp.mongo            = mongo
logged_home_page_bp.mongo = mongo

# Registra i blueprint
app.register_blueprint(registrazione_bp, url_prefix='/registrazione')
app.register_blueprint(login_bp, url_prefix='/login')
app.register_blueprint(voti_bp, url_prefix='')
app.register_blueprint(stati_bp, url_prefix='')
app.register_blueprint(logged_home_page_bp, url_prefix='')


@app.route('/')
def home():
    if 'id_utente' in session:
        return redirect(url_for('logged_home_page.logged_home_page'))
    return render_template('index.html')


@app.route('/lista')
def lista():
    if 'id_utente' not in session:
        return redirect(url_for('login.login'))

    id_utente = session.get('id_utente')
    utente = mongo.db.utenti.find_one({"_id": ObjectId(id_utente)})

    film_list = []
    if utente and 'filmVisti' in utente:
        filmVisti = [f for f in utente['filmVisti'] if f['stato'] in ['visto', 'da vedere']]
        film_ids = [f['film_id'] for f in filmVisti]

        film_list = list(mongo.db.films.find({'_id': {'$in': film_ids}}))

        # Mappa _id stringa -> voto e stato
        stato_voto_map = {str(f['film_id']): {'voto': f.get('voto'), 'stato': f.get('stato')} for f in filmVisti}

        for film in film_list:
            film['_id'] = str(film['_id'])
            film['voto_utente'] = int(stato_voto_map[film['_id']]['voto']) if stato_voto_map[film['_id']]['voto'] is not None else 0
            film['stato_utente'] = stato_voto_map[film['_id']]['stato']

    # Passa anche la variabile utente_loggato per template
    utente_loggato = 'id_utente' in session
    username = utente.get('username') if utente else None

    return render_template('lista.html', film_list=film_list, utente_loggato=utente_loggato, username=username)


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

    username = utente.get('username') if utente else None

    return render_template('movie-card.html', film=film, consigliati=consigliati,
                           utente_loggato=utente_loggato,
                           voto_utente=voto_utente,
                           stato_utente=stato_utente,
                           username=username)



@app.route('/logout')
def logout():
    session.clear()  # Cancella tutta la sessione
    return redirect(url_for('registrazione.registrazione'))  # O dove vuoi reindirizzare


if __name__ == "__main__":
    app.run(debug=True)
