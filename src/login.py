from flask import Blueprint, render_template, request, redirect, url_for, flash

login_bp = Blueprint('registrazione', __name__)


@login_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        utente_esistente = login_bp.mongo.db.utenti.find_one({
            "$or": [
                {"username": username},
                {"email"   : username}        
            ]
        })

        if not utente_esistente:
            flash("Utente non trovato!", "errore")
            return render_template(url_for('registrazione.registrazione'), show_login = True)


        return redirect(url_for('logged_home_page'))
    # Se invece è una richiesta GET
    return render_template('registrazione.html')