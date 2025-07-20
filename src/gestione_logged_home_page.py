from bson import ObjectId
from flask import session, redirect, url_for, render_template, Blueprint
from pymongo import MongoClient

logged_home_page_bp = Blueprint('logged_home_page', __name__)

client = MongoClient()
db     = client.cinematch

# check if the user is in session
def get_utente():
    id_utente = session.get('id_utente')
    if not id_utente:
        return None
    utente = db.utenti.find_one({"_id": ObjectId(id_utente)})
    return utente


# retrieve the username of the user in session
def get_username():
    utente = get_utente()
    if not utente:
        return None
    return utente.get('username')


# retrieves the ID of the films that the user has seen or intends to see
def get_film_visti_ids():
    utente = get_utente()
    if not utente:
        return []

    return [
        film['film_id']
        for film in utente.get('filmVisti', [])
        if (film.get('stato') == 'visto' or film.get('stato') == 'da vedere') and 'film_id' in film
    ]


# retrievs films watched by the user
def get_film_visti(film_visti_ids):
    if not film_visti_ids:
        return []
    return list(db.films.find({'_id': {'$in': film_visti_ids}}))


# get the latest film 
def get_ultime_uscite():
    ultime_uscite = list(db.films.aggregate([
        {'$match': {'uscita': {'$gte': '2018'}}},
        {'$sample': {'size': 5}}
    ]))
    return ultime_uscite


# get the most popular film among users
def get_film_popolari():
    popolari_agg = db.utenti.aggregate([
        {"$unwind": "$filmVisti"},
        {"$match": {"filmVisti.stato": {"$in": ["visto", "da vedere"]}}},
        {"$group": {
            "_id": "$filmVisti.film_id",
            "count": {"$sum": 1}
        }},
        {"$sort": {"count": -1}},
        {"$limit": 16}
    ])

    film_popolari_ids = [doc["_id"] for doc in popolari_agg]
    film_popolari = list(db.films.find({"_id": {"$in": film_popolari_ids}}))

    return film_popolari


# get list based on session user taste
def get_lista_gusti(film_visti, film_visti_ids):
    generi_preferiti = list({film['genere'] for film in film_visti if 'genere' in film})

    lista_gusti = list(db.films.aggregate([
        {
            '$match': {
                'genere': {'$in': generi_preferiti},
                '_id': {'$nin': film_visti_ids}
            }
        },
        {'$sample': {'size': 16}}
    ]))

    return lista_gusti



@logged_home_page_bp.route('/logged-home-page', methods=['GET'])
def logged_home_page():
    username = get_username()
    if not username:
        return redirect(url_for('login.login'))

    film_visti_ids = get_film_visti_ids()
    film_visti     = get_film_visti(film_visti_ids)
    ultime_uscite  = get_ultime_uscite()
    film_popolari  = get_film_popolari()
    lista_gusti    = get_lista_gusti(film_visti, film_visti_ids)

    return render_template(
        'logged-home-page.html',
        lista_gusti=lista_gusti,
        film_popolari=film_popolari,
        ultime_uscite=ultime_uscite,
        username=username
    )

