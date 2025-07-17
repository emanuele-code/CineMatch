from flask import Flask, render_template
from flask_pymongo import PyMongo
from src.registrazione import registrazione_bp  # import blueprint
from src.login import login_bp

app = Flask(__name__)
app.secret_key = 'key' # serve a flask per gestire la seessione ad esempio per usare flash() che richiede una sessione per funzionare

# Configura la connessione a MongoDB, MongoDB gira su porta logica 27017 
app.config["MONGO_URI"] = "mongodb://localhost:27017/cinematch"

# Inizializza Flask-PyMongo
mongo = PyMongo(app)

# Passo la connessione mongo al blueprint così può usarla
registrazione_bp.mongo = mongo
login_bp.mongo         = mongo

# Registra il blueprint nella app
app.register_blueprint(registrazione_bp, url_prefix='/registrazione')
app.register_blueprint(login_bp, url_prefix='/login')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/lista')
def lista():
    # mongoDB ritorna documenti con _id in formato ObjectId, converto in stringa per Jinja
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

    return render_template('movie-card.html', film=film, consigliati=consigliati)


@app.route('/logged-home-page')
def logged_home_page():
    film_list = list(mongo.db.films.find())
    for film in film_list:
        film['_id'] = str(film['id'])
    return render_template('logged-home-page.html', film_list=film_list)



if __name__ == "__main__":
    app.run(debug=True)
