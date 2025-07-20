# login.py
from flask import Blueprint, render_template, request, flash, redirect, url_for, session

login_bp = Blueprint('login', __name__)

@login_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        utente_esistente = login_bp.mongo.db.utenti.find_one({
            "$or": [
                {"username": username},
                {"email": username}
            ]
        })

        if not utente_esistente:
            flash("Credenziali errate!", "errore")
            # Ritorna il template direttamente
            return render_template('registrazione.html', show_login=True)
        else:   
            session['id_utente'] = str(utente_esistente['_id'])
            return redirect(url_for('logged_home_page.logged_home_page'))   

    return render_template('registrazione.html', show_login=True)
