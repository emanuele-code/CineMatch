from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash

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
            return redirect(url_for('registrazione.registrazione'))

        hashed_pw = generate_password_hash(password)
        registrazione_bp.mongo.db.utenti.insert_one({
            "username": username,
            "email": email,
            "password": hashed_pw,
            "filmVisti": []
        })

        flash("Registrazione avvenuta con successo! Effettua il login.")
    from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash

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
            return redirect(url_for('registrazione.registrazione'))

        hashed_pw = generate_password_hash(password)
        registrazione_bp.mongo.db.utenti.insert_one({
            "username": username,
            "email": email,
            "password": hashed_pw,
            "filmVisti": []
        })

        return redirect(url_for('logged_home_page'))
    # Se invece è una richiesta GET
    return render_template('registrazione.html')