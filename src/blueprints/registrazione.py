from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash

# create blueprint for registration
registrazione_bp = Blueprint('registrazione_bp', __name__)

# handle registration (GET = show form, POST = save new user)
@registrazione_bp.route('/', methods=['GET', 'POST'])
def registrazione():

    if request.method == 'POST':
        username = request.form.get('username')
        email    = request.form.get('email')
        password = request.form.get('password')

        # check if the email is already registered
        utente_esistente = registrazione_bp.mongo.db.utenti.find_one({"email": email})
        if utente_esistente:
            flash("Email già registrata!", "errore")
            return render_template('registrazione.html', show_login=False)

        # create new user with hashed password
        hashed_pw = generate_password_hash(password)
        result    = registrazione_bp.mongo.db.utenti.insert_one({
            "username" : username,
            "email"    : email,
            "password" : hashed_pw,
            "filmVisti": []
        })

        # save user id in session to keep login
        session['id_utente'] = str(result.inserted_id)
        return redirect(url_for('logged_home_page_bp.logged_home_page'))

    # GET: show registration form
    return render_template('registrazione.html', show_login=False)
