from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash

# il primo attributo è il nome del BP (sto usando url_for) il secondo __name__ identifica il modulo in cui si trova il BP
# è come se dicesse: il modulo si trova in questo relative path
registrazione_bp = Blueprint('registrazione', __name__)


@registrazione_bp.route('/', methods=['GET', 'POST'])
def registrazione():
    if request.method == 'POST':
        username = request.form.get('username')
        email    = request.form.get('email')
        password = request.form.get('password')

        utente_esistente = registrazione_bp.mongo.db.utenti.find_one({"email": email})
        if utente_esistente:
            flash("Email già registrata!", "errore")
            return render_template('registrazione.html', show_login=False)

        hashed_pw = generate_password_hash(password)
        registrazione_bp.mongo.db.utenti.insert_one({
            "username": username,
            "email": email,
            "password": hashed_pw,
            "filmVisti": []
        })

        id_utente['id_utente'] = str(utente_esistente['_id'])
        return redirect(url_for('logged_home_page'))
    # Se invece è una richiesta GET
    return render_template('registrazione.html', show_login = False)