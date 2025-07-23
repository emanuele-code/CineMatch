from flask   import Blueprint, jsonify, redirect, render_template, request, session, url_for
from bson    import ObjectId
from pymongo import MongoClient

lista_bp = Blueprint('lista_bp', __name__)

client = MongoClient()
db     = client.cinematch
films  = db.films
utenti = db.utenti



@lista_bp.route('/')
def lista():
    # check if the user is in session
    if 'id_utente' not in session:
        return redirect(url_for('login_bp.login'))

    # get user id in session and return the user with that id from the collection in mongodb
    id_utente = session.get('id_utente')
    utente    = utenti.find_one({"_id": ObjectId(id_utente)})

    film_list = []
    if utente and 'filmVisti' in utente:
        # Filter the user's 'filmVisti' list to include only films with status 'visto' or 'da vedere'
        # Extract the 'film_id' from each filtered film entry
        # Query the 'films' collection to retrieve all film documents whose '_id' is in the list of film_ids
        filmVisti = [f for f in utente['filmVisti'] if f['stato'] in ['visto', 'da vedere']]
        film_ids = [f['film_id'] for f in filmVisti]
        film_list = list(films.find({'_id': {'$in': film_ids}}))

        # Create a dictionary mapping each film's ID (as a string) to its user's vote ('voto')
        #  and status ('stato') from 'filmVisti'        
        stato_voto_map = {str(f['film_id']): {'voto': f.get('voto'), 'stato': f.get('stato')} for f in filmVisti}
        for film in film_list:
            # convert the film's _id from ObjectId to string because python dict is based on str
            # Add the user's vote for the film, converting to int; if no vote exists, default to 0
            # Add the user's status ('stato') for the film (visto, da vedere, nessuno)
            film['_id'] = str(film['_id'])
            film['voto_utente'] = int(stato_voto_map[film['_id']]['voto']) if stato_voto_map[film['_id']]['voto'] is not None else 0
            film['stato_utente'] = stato_voto_map[film['_id']]['stato']

    utente_loggato = 'id_utente' in session
    username = utente.get('username') if utente else None
    
    # get unique genres to fill the front-end filter
    generi_unici = films.distinct("genere")

    return render_template('lista.html', film_list=film_list, utente_loggato=utente_loggato, username=username, generi_unici=generi_unici)

