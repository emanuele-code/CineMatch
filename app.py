import os
from flask                                     import Flask, render_template, session, redirect, url_for, request, jsonify
from flask_pymongo                             import PyMongo
from bson.objectid                             import ObjectId
from src.blueprints.registrazione              import registrazione_bp  # import blueprint
from src.blueprints.login                      import login_bp
from src.blueprints.gestione_voti              import voti_bp
from src.blueprints.gestione_stati             import stati_bp
from src.blueprints.gestione_logged_home_page  import logged_home_page_bp
from src.blueprints.gestione_movie_card        import movie_card_bp
from src.blueprints.gestione_lista             import lista_bp


# Flask() creates the application, while __name__ is used to retrieve the relative path of the main file
def crea_app():
    app = Flask(__name__)

    # is used by flask to handle the session
    app.secret_key = 'key'  

    # Configure connection to MongoDB
    # app.config["MONGO_URI"] = "mongodb://localhost:27017/cinematch" #hardcoded
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/cinematch")
    app.config["MONGO_URI"] = mongo_uri

    # init Flask-PyMongo
    mongo = PyMongo(app)

    # pass the mongo connection to the blueprint
    registrazione_bp.mongo    = mongo
    login_bp.mongo            = mongo
    voti_bp.mongo             = mongo
    stati_bp.mongo            = mongo
    logged_home_page_bp.mongo = mongo
    movie_card_bp.mongo       = mongo
    lista_bp.mongo            = mongo


    # The first argument is the instance of the Blueprint created in the corresponding module,
    # the second is the prefix that every URL in that module must start with.
    # For example, invia_registrazione
    app.register_blueprint(registrazione_bp,    url_prefix='/registrazione') # pages
    app.register_blueprint(login_bp,            url_prefix='/login')
    app.register_blueprint(lista_bp,            url_prefix='/lista')
    app.register_blueprint(movie_card_bp,       url_prefix='') # utilities functions
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
        session.clear()  # delete the whole session
        return redirect(url_for('registrazione_bp.registrazione'))  
    
    return app
    

# notify that this is the main entry point of the logic in the code
if __name__ == "__main__":
    app = crea_app()
    app.run(debug=True)
