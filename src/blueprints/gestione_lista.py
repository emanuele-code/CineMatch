from flask   import Blueprint, jsonify, redirect, render_template, request, session, url_for
from bson    import ObjectId
from pymongo import MongoClient

lista_bp = Blueprint('lista_bp', __name__)

@lista_bp.route('/')
def lista():
    films  = lista_bp.mongo.db.films        
    utenti = lista_bp.mongo.db.utenti        

    # check if user is logged in
    if 'id_utente' not in session:
        return redirect(url_for('login_bp.login'))

    # get user from session
    id_utente = session.get('id_utente')
    utente    = utenti.find_one({"_id": ObjectId(id_utente)})

    film_list = []
    if utente and 'filmVisti' in utente:
        # filter movies that are seen or to-watch
        filmVisti = [f for f in utente['filmVisti'] if f.get('stato') in ['visto', 'da vedere']]
        film_ids  = [f['film_id'] for f in filmVisti]
        # get movie documents corresponding to the ids
        film_list = list(films.find({'_id': {'$in': film_ids}}))

        # map film_id -> user's rating and status
        stato_voto_map = {str(f['film_id']): {'voto': f.get('voto'), 'stato': f.get('stato')} for f in filmVisti}
        for film in film_list:
            film['_id'] = str(film['_id'])  # convert ObjectId to string
            film['voto_utente']  = int(stato_voto_map[film['_id']]['voto']) if stato_voto_map[film['_id']]['voto'] is not None else 0
            film['stato_utente'] = stato_voto_map[film['_id']]['stato']

    utente_loggato = 'id_utente' in session
    username       = utente.get('username') if utente else None
    
    # generate unique genres for front-end filters
    generi_unici = films.distinct("genere")

    return render_template('lista.html', film_list=film_list, utente_loggato=utente_loggato, username=username, generi_unici=generi_unici)
