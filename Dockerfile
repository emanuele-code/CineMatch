# Usa l'immagine ufficiale di Python 3.11 in versione slim come base leggera
FROM python:3.11-slim

# Imposta la cartella di lavoro all'interno del container
# Tutti i comandi successivi saranno eseguiti in questa cartella
WORKDIR /app

# Copia il file requirements.txt nel container
COPY requirements.txt .

# Installa tutte le dipendenze elencate in requirements.txt
# --no-cache-dir evita di salvare la cache dei pacchetti per risparmiare spazio
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il codice dell’app nel container
COPY . .

# Espone la porta 5000, quella su cui Flask sarà in ascolto
EXPOSE 5000

# Imposta le variabili d'ambiente per Flask
# FLASK_APP indica il modulo e la funzione che crea l'app Flask
# FLASK_RUN_HOST 0.0.0.0 permette di accedere a Flask dall'esterno del container
ENV FLASK_APP=app:crea_app
ENV FLASK_RUN_HOST=0.0.0.0

# Comando che viene eseguito all'avvio del container
# Avvia l'app Flask in modalità server di sviluppo
CMD ["flask", "run"]
