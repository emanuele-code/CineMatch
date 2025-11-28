# Cinematch

The application allows users to receive movie recommendations, write reviews, and share opinions. Titles cannot be searched directly: the idea is that suggestions come in a guided way, encouraging the discovery of new films without searching for them manually, fostering a more spontaneous experience based on community recommendations.

## Requirements

- Docker and Docker Compose installed
- Web browser

---

## Starting the app

1. Clone the repository (if needed):

```bash
git clone <URL-of-repo>
cd <folder-name>
````

## Build and start the container

From terminal:

```
docker compose up --build
```

This command builds the images and starts two services:

`mongo`: the MongoDB database

`web`: the Flask application

Open your browser and go to:

```
http://127.0.0.1:5000
```

## Useful commands

* Rebuild and update containers after changes:

```
docker compose up --build
```

* Check container status:

```
docker compose ps
```

* View Flask logs:

```
docker compose logs -f web
```

* View Mongo logs:

```
docker compose logs -f mongo
```

* Stop containers:

```
docker compose down
```

* Remove Docker volumes:

```
docker compose down -v
```

