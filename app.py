from flask                         import Flask, render_template, session, redirect, url_for, request, jsonify
from flask_pymongo                 import PyMongo
from bson.objectid                 import ObjectId
from src.registrazione             import registrazione_bp  # import blueprint
from src.login                     import login_bp
from src.gestione_voti             import voti_bp
from src.gestione_stati            import stati_bp
from src.gestione_logged_home_page import logged_home_page_bp
from src.gestione_movie_card       import movie_card_bp
from src.gestione_lista            import lista_bp

# Flask() crea l´applicazione mentre __name__ recupera a recuperare il percorso relativo al file principale
app = Flask(__name__)

# serve a flask per gestire la sessione
app.secret_key = 'key'  

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
movie_card_bp.mongo       = mongo
lista_bp.mongo            = mongo

# il primo argomento è l'istanza di Bp creata nel modulo corrispondente, il secondo è il prefisso
# secondo il quale qualsiasi URL in suddetto modulo deve iniziare 
# ad esempio invia_registrazione 
app.register_blueprint(registrazione_bp,    url_prefix='/registrazione')
app.register_blueprint(login_bp,            url_prefix='/login')
app.register_blueprint(lista_bp,            url_prefix='/lista')
app.register_blueprint(movie_card_bp,       url_prefix='')
app.register_blueprint(voti_bp,             url_prefix='')
app.register_blueprint(stati_bp,            url_prefix='')
app.register_blueprint(logged_home_page_bp, url_prefix='')


@app.route('/')
def home():
    if 'id_utente' in session:
        return redirect(url_for('logged_home_page_bp.logged_home_page'))
    return render_template('landing-page.html')



@app.route('/logout')
def logout():
    session.clear()  # Cancella tutta la sessione
    return redirect(url_for('registrazione_bp.registrazione'))  


if __name__ == "__main__":
    app.run(debug=True)
