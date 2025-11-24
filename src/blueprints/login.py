from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from werkzeug.security import check_password_hash

login_bp = Blueprint('login_bp', __name__)

# handle login (GET = show form, POST = process login)
@login_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # search for user by username or email
        utente_esistente = login_bp.mongo.db.utenti.find_one({
            "$or": [
                {"username": username},
                {"email"   : username}
            ]
        })

        # user not found
        if not utente_esistente:
            flash("Credenziali errate!", "errore")
            return render_template('registrazione.html', show_login=True)
        else:          
            # check password
            if not check_password_hash(utente_esistente['password'], password):
                flash("Credenziali errate!", "errore")
                return render_template('registrazione.html', show_login=True)

            # successful login, save id in session
            session['id_utente'] = str(utente_esistente['_id'])
            return redirect(url_for('logged_home_page_bp.logged_home_page'))   

    # GET: show login form
    return render_template('registrazione.html', show_login=True)
