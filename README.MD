# Cinematch

Applicazione web Flask per gestire film, utenti e recensioni, con database MongoDB.

## Requisiti

- Docker e Docker Compose installati
- Browser web

---

## Avvio dell’app

1. Clona il repository (se necessario):

```bash
git clone <URL-del-repo>
cd <nome-cartella>
````

## Costruisce ed avvia il container
Da terminale

````
docker compose up --build
````

Questo comando costruisce le immagini e avvia due servizi:

`mongo`: il database MongoDB

`web`: l’app Flask

Apri il browser e vai su:
````
http://localhost:5000
````



## Comandi utili 
* Ricostruire e aggiornare i container dopo modifice:
````
docker compose up --build
````

* Controlla lo stato del container:
````
docker compose ps
````

* vedere i log di Flask:
````
docker compose logs -f web
````

* Vedere i log di mongo:
````
docker compose logs -f mongo
````

* Fermare i container:
````
docker compose down
````

* Per rimuovere i volumi da Docker:
````
docker compose down -v
````







