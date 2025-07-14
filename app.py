from flask import Flask, render_template

app = Flask(__name__)

film_list = [
    {
        'id': 1,
        'titolo': '28 Years Later',
        'stelle': 4,
        'regista': 'Alex Garland',
        'uscita': '2025',
        'stato': 'visto',
        'genere': 'Horror',
        'immagine': 'images/28-Years-Later.jpg',
        'trama': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque dignissim hendrerit augue, vitae aliquam dui volutpat non. Donec tempor arcu quis est finibus faucibus. Aenean vel venenatis turpis. Sed vitae egestas eros. Nulla facilisi. Morbi condimentum leo vel maximus sodales. Ut placerat auctor lorem, vitae volutpat sem volutpat eu. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Praesent erat massa, maximus ac mauris eget, iaculis rutrum dui. Fusce dapibus at ex eget pretium. Vivamus pharetra lacinia quam. Suspendisse sit amet elit convallis orci bibendum varius ut a augue. Sed euismod, dui consequat vehicula semper, purus tortor fermentum lectus, non iaculis tortor ligula et ante. Aliquam erat volutpat. Suspendisse quis lectus fermentum, hendrerit orci in, mattis turpis. '
    },
    {
        'id': 2,
        'titolo': 'Elio',
        'stelle': 3,
        'regista': 'Adrian Molina',
        'uscita': '2025',
        'stato': 'da-vedere',
        'genere': 'Animazione',
        'immagine': 'images/elio.jpg',
        'trama': 'Un ragazzo viene scelto dagli alieni per rappresentare l’umanità.'
    },
    {
        'id': 3,
        'titolo': 'Sorry, Baby',
        'stelle': 5,
        'regista': 'Emma Seligman',
        'uscita': '2024',
        'stato': 'visto',
        'genere': 'Drammatico',
        'immagine': 'images/sorry-baby.jpg',
        'trama': 'Una storia intensa su relazioni, identità e crescita personale.'
    },
    {
        'id': 4,
        'titolo': 'Real Steel',
        'stelle': 4,
        'regista': 'Shawn Levy',
        'uscita': '2011',
        'stato': 'visto',
        'genere': 'Sci-Fi',
        'immagine': 'images/real-steel.jpg',
        'trama': 'In un futuro dove i robot combattono al posto degli umani, un padre e un figlio si avvicinano grazie alla boxe.'
    },
    {
        'id': 5,
        'titolo': '30 Years Later',
        'stelle': 4,
        'regista': 'Alex Garland',
        'uscita': '2025',
        'stato': 'visto',
        'genere': 'Horror',
        'immagine': 'images/28-Years-Later.jpg',
        'trama': ''
    },
    {
        'id': 6,
        'titolo': '30 Years Later',
        'stelle': 4,
        'regista': 'Alex Garland',
        'uscita': '2025',
        'stato': 'visto',
        'genere': 'Horror',
        'immagine': 'images/28-Years-Later.jpg',
        'trama': ''
    },
    {
        'id': 7,
        'titolo': '30 Years Later',
        'stelle': 4,
        'regista': 'Alex Garland',
        'uscita': '2025',
        'stato': 'visto',
        'genere': 'Horror',
        'immagine': 'images/28-Years-Later.jpg',
        'trama': ''
    },
    {
        'id': 8,
        'titolo': '30 Years Later',
        'stelle': 4,
        'regista': 'Alex Garland',
        'uscita': '2025',
        'stato': 'visto',
        'genere': 'Horror',
        'immagine': 'images/28-Years-Later.jpg',
        'trama': ''
    },
    {
        'id': 9,
        'titolo': '30 Years Later',
        'stelle': 4,
        'regista': 'Alex Garland',
        'uscita': '2025',
        'stato': 'visto',
        'genere': 'Horror',
        'immagine': 'images/28-Years-Later.jpg',
        'trama': ''
    }
]

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/registrazione')
def registrazione():
    return render_template('registrazione.html')


@app.route('/lista')
def lista():
    return render_template('lista.html', film_list=film_list)
    


@app.route('/movie-card/<int:film_id>')
def movie_card(film_id):
    film = next((f for f in film_list if f['id'] == film_id), None)

    if film is None:
        return "Film non trovato", 404

    # Film simili (consigliati) – esempio semplice per ora
    consigliati = [f for f in film_list if f['genere'] == film['genere'] and f['id'] != film_id]

    return render_template('movie-card.html', film=film, consigliati=consigliati)


@app.route('/logged-home-page')
def logged_home_page():
    return render_template('logged-home-page.html', film_list=film_list)



if __name__ == "__main__":
    app.run(debug=True)
