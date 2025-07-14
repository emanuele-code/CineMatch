from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/registrazione')
def registrazione():
    return render_template('registrazione.html')

@app.route('/lista')
def lista():
    film_list = [
        {
            'titolo': '28 Years Later',
            'stelle': 4,
            'regista': 'Alex Garland',
            'uscita': '2025',
            'stato': 'visto',
            'genere': 'Horror',
            'immagine': 'images/28-Years-Later.jpg'
        },
        {
            'titolo': 'Elio',
            'stelle': 3,
            'regista': 'Adrian Molina',
            'uscita': '2025',
            'stato': 'da-vedere',
            'genere': 'Animazione',
            'immagine': 'images/elio.jpg'
        },
        {
            'titolo': 'Sorry, Baby',
            'stelle': 5,
            'regista': 'Emma Seligman',
            'uscita': '2024',
            'stato': 'visto',
            'genere': 'drammatico',
            'immagine': 'images/sorry-baby.jpg'
        },
        {
            'titolo': 'Real steel',
            'stelle': 4,
            'regista': 'Shawn Levy',
            'uscita': '2011',
            'stato': 'visto',
            'genere': 'Sci-Fi',
            'immagine': 'images/real-steel.jpg'
        }
    ]
    return render_template('lista.html', film_list=film_list)

if __name__ == "__main__":
    app.run(debug=True)
