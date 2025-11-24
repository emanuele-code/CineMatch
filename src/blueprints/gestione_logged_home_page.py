from bson import ObjectId
from flask import session, redirect, url_for, render_template, Blueprint
from pymongo import MongoClient

logged_home_page_bp = Blueprint('logged_home_page_bp', __name__)

# returns the logged-in user or None
def get_utente():
    db = logged_home_page_bp.mongo.db
    id_utente = session.get('id_utente')
    if not id_utente:
        return None
    return db.utenti.find_one({"_id": ObjectId(id_utente)})

# returns the username of the logged-in user
def get_username():
    utente = get_utente()
    return utente.get('username') if utente else None

# returns the _id of movies marked as seen or to-watch
def get_film_visti_ids():
    utente = get_utente()
    if not utente:
        return []
    return [
        film['film_id']
        for film in utente.get('filmVisti', [])
        if film.get('stato') in ['visto', 'da vedere'] and 'film_id' in film
    ]

# returns the movie documents corresponding to the ids
def get_film_visti(film_visti_ids):
    db = logged_home_page_bp.mongo.db
    if not film_visti_ids:
        return []
    return list(db.films.find({'_id': {'$in': film_visti_ids}}))

# fetches the latest releases since 2018 (5 random)
def get_ultime_uscite():
    db = logged_home_page_bp.mongo.db
    return list(db.films.aggregate([
        {'$match': {'uscita': {'$gte': '2018'}}},
        {'$sample': {'size': 5}}
    ]))

# fetches the most popular movies among users (max 16)
def get_film_popolari():
    db = logged_home_page_bp.mongo.db
    agg = db.utenti.aggregate([      # get documents from the collection and filter through the stages below
        {"$unwind": "$filmVisti"},  # explode the array into single documents
        {"$match": {"filmVisti.stato": {"$in": ["visto", "da vedere"]}}}, # keep only documents with these states
        {"$group": {"_id": "$filmVisti.film_id", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 16}
    ])
    film_ids = [doc["_id"] for doc in agg]
    return list(db.films.find({"_id": {"$in": film_ids}}))

# fetches a random list of movies (16)
def get_lista_random():
    db = logged_home_page_bp.mongo.db
    return list(db.films.aggregate([{'$sample': {'size': 16}}]))

# main route for logged-in users
@logged_home_page_bp.route('/logged-home-page', methods=['GET'])
def logged_home_page():
    username = get_username()
    if not username:
        return redirect(url_for('login_bp.login'))
    
    ultime_uscite  = get_ultime_uscite()
    film_popolari  = get_film_popolari()
    lista_random    = get_lista_random()

    return render_template(
        'logged-home-page.html',
        lista_random  = lista_random,
        film_popolari = film_popolari,
        ultime_uscite = ultime_uscite,
        username      = username
    )
