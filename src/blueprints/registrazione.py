from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash

# crea blueprint per la registrazione
registrazione_bp = Blueprint('registrazione_bp', __name__)

# gestisce registrazione (GET = mostra form, POST = salva nuovo utente)
@registrazione_bp.route('/', methods=['GET', 'POST'])
def registrazione():

    if request.method == 'POST':
        username = request.form.get('username')
        email    = request.form.get('email')
        password = request.form.get('password')

        # verifica se l'email è già registrata
        utente_esistente = registrazione_bp.mongo.db.utenti.find_one({"email": email})
        if utente_esistente:
            flash("Email già registrata!", "errore")
            return render_template('registrazione.html', show_login=False)

        # crea nuovo utente con password hashata
        hashed_pw = generate_password_hash(password)
        result    = registrazione_bp.mongo.db.utenti.insert_one({
            "username" : username,
            "email"    : email,
            "password" : hashed_pw,
            "filmVisti": []
        })

        # salva id utente in sessione per mantenere login
        session['id_utente'] = str(result.inserted_id)
        return redirect(url_for('logged_home_page_bp.logged_home_page'))

    # GET: mostra form di registrazione
    return render_template('registrazione.html', show_login=False)
