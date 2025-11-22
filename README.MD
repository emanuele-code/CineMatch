
# Come avviare CineMatch

## Prerequisiti
- Python 3
- MongoDB

## Installazione e configurazione

1. **Apri la cartella del progetto**
```bash
cd CineMatch
````

2. **Crea ed attiva un ambiente virtuale**

   * Se l'ambiente virtuale non è stato ancora creato:

     ```bash
     python3 -m venv venv
     ```
   * Attivalo con:

     ```bash
     source venv/bin/activate
     ```

3. **Installa le dipendenze utili**

   ```bash
   pip install -r requirements.txt
   ```

4. **Avvia MongoDB**

   ```bash
   sudo systemctl start mongod
   ```
    Tip: In molti setup di sviluppo, MongoDB potrebbe già essere avviato in automatico (per esempio, può essere avviato da servizi di sistema o altri strumenti).
    Se è già attivo un processo mongodb, puoi skippare questo passo - L'applicazione Flask si connette all'istanza già avviata di mongoDB

    Puoi verificare se mongodb è avviato provando ad accedere alla sua shell:
    ```bash
    mongosh
    ```
    Si dovrebbe connettere a mongodb//127.0.0.1:27017

6. **Popola il database**
   
   per testare possiamo popolare il database con film ed utenti (gli utenti li possiamo anche creare dinamicamente senza caricarli nel database da file)

   * andare sul terminale aprire la shell di mongodb con l'istruzione `mongosh`
   * apri/crea il database con l'istruzione `use cinematch`
   * apri il file `cinematch_db.txt` e copia prima tutta la query `db.films.insertMany([...])` e incollala nella shell mongosh e clicca invio
   * ripeti lo stesso passaggio per la query `db.utenti.insertMany([...])`
   *  il terminale

5. **Avvia l'app Flask**

   ```bash
   export FLASK_APP=app.py
   flask run
   ```

6. **Accedi all'app**
   Apri il browser e visita:

   ```
   http://127.0.0.1:5000
   ```

## Note

* Assicurati che mongodb sia stato avviato prima di avviare l'app.
* L'app è avviata su porta `5000`.