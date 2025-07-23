from flask import Blueprint, jsonify, redirect, render_template, request, session, url_for
from bson import ObjectId
from pymongo import MongoClient

lista_bp = Blueprint('lista', __name__)

client = MongoClient()
db     = client.cinematch
films  = db.films
utenti = db.utenti



@lista_bp.route('/')
def lista():
    if 'id_utente' not in session:
        return redirect(url_for('login.login'))

    id_utente = session.get('id_utente')
    utente = utenti.find_one({"_id": ObjectId(id_utente)})

    film_list = []
    if utente and 'filmVisti' in utente:
        filmVisti = [f for f in utente['filmVisti'] if f['stato'] in ['visto', 'da vedere']]
        film_ids = [f['film_id'] for f in filmVisti]

        film_list = list(films.find({'_id': {'$in': film_ids}}))

        # Mappa _id stringa -> voto e stato
        stato_voto_map = {str(f['film_id']): {'voto': f.get('voto'), 'stato': f.get('stato')} for f in filmVisti}

        for film in film_list:
            film['_id'] = str(film['_id'])
            film['voto_utente'] = int(stato_voto_map[film['_id']]['voto']) if stato_voto_map[film['_id']]['voto'] is not None else 0
            film['stato_utente'] = stato_voto_map[film['_id']]['stato']

    # Passa anche la variabile utente_loggato per template
    utente_loggato = 'id_utente' in session
    username = utente.get('username') if utente else None

    generi_unici = films.distinct("genere")

    return render_template('lista.html', film_list=film_list, utente_loggato=utente_loggato, username=username, generi_unici=generi_unici)

