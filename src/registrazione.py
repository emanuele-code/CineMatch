from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash



# the first attribute is the name of the BP (I'm using url_for) the second __name__ identifies the module where the BP is located
# it's as if it were saying: the module is found in this relative path
registrazione_bp = Blueprint('registrazione_bp', __name__)



# Bind the function below to the root URL ('/') of the 'bp_registration' blueprint;
# accepts HTTP requests of the GET type (to show the page) and POST (to send data from the form).
@registrazione_bp.route('/', methods=['GET', 'POST'])
def registrazione():

    if request.method == 'POST':
        username = request.form.get('username')
        email    = request.form.get('email')
        password = request.form.get('password')

        # check if there is a user with the email you entered, if there is it gives me an error and reloads the page
        utente_esistente = registrazione_bp.mongo.db.utenti.find_one({"email": email})
        if utente_esistente:
            flash("Email già registrata!", "errore")
            return render_template('registrazione.html', show_login=False)

        # if the user doesn't exist it will hash its password and create a new user in the collection
        hashed_pw = generate_password_hash(password)
        result    = registrazione_bp.mongo.db.utenti.insert_one({
            "username" : username,
            "email"    : email,
            "password" : hashed_pw,
            "filmVisti": []
        })

        # Store the newly created user's unique ID in the session as a string,
        # so the app can recognize and keep the user logged in across requests.
        session['id_utente'] = str(result.inserted_id)
        return redirect(url_for('logged_home_page.logged_home_page'))

    return render_template('registrazione.html', show_login=False)
