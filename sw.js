const cacheName = 'pwaCinematch';

const cacheList = [
    '/', // L'indice della tua app (fondamentale per l'esperienza offline)
    '/manifest.json',

    // css
    '/static/css/style-landing-page.css',
    '/static/css/style-lista.css',
    '/static/css/style-logged-home-page.css',
    '/static/css/style-movie-card.css',
    '/static/css/style-registrazione.css',

    // javascript
    '/static/javascript/aggiorna-stato.js',
    '/static/javascript/carosello.js',
    '/static/javascript/filtro-lista.js',
    '/static/javascript/registrazione-toggle.js',
    '/static/javascript/set-stars.js',
    '/static/javascript/star-animation.js',
    '/static/javascript/toggle-droplist.js',
    '/static/javascript/toggle-review-textarea.js',
    '/static/javascript/toggle-user-menu.js',

    // images
    '/static/images/clapperboard.jpg', //icon
    '/static/images/28-Years-Later.jpg',
    '/static/images/arrival.jpg',
    '/static/images/big-hero-6.jpeg', 
    '/static/images/big-hero-6.jpg', 
    '/static/images/blackpanther.jpg',
    '/static/images/bladerunner2049.jpg',
    '/static/images/cinema_background.jpg',
    '/static/images/coco.jpg',
    '/static/images/dark-knight.jpg',
    '/static/images/dune.jpg',
    '/static/images/elio.jpg',
    '/static/images/finding-nemo.jpg',
    '/static/images/frozen.jpg',
    '/static/images/gladiator.jpg',
    '/static/images/guardians.jpg',
    '/static/images/how-to-train-your-dragon.jpg',
    '/static/images/inception.jpg',
    '/static/images/incredibles.jpg',
    '/static/images/inglorious-basterds.jpg',
    '/static/images/inside-out.jpg',
    '/static/images/interstellar.jpg',
    '/static/images/kubo.jpg',
    '/static/images/lion-king.jpg',
    '/static/images/madmax.jpg',
    '/static/images/martian.jpg',
    '/static/images/matrix.jpg',
    '/static/images/monsters-inc.jpg',
    '/static/images/myheroacademia-rising.jpg',
    '/static/images/pulp-fiction.jpg',
    '/static/images/ratatouille.jpg',
    '/static/images/real-steel.jpg',
    '/static/images/sorry-baby.jpg',
    '/static/images/spirited-away.jpg',
    '/static/images/tenet.jpg',
    '/static/images/toy-story.jpg',
    '/static/images/your-name.jpg',
];



// 1. 'install' event: Precaching of essential assets
self.addEventListener('install', e => {
    console.log('Service Worker: Installazione avviata');
    e.waitUntil(
        caches.open(cacheName)
            .then(cache => {
                // add every file from the cachelist to the cache.
                return cache.addAll(cacheList); 
            })
    );
});



// 2. 'fetch': it cache first and then ask to the network and save in cache 
self.addEventListener('fetch', event => {

    event.respondWith(
        caches.match(event.request).then(cached => {
            if (cached) {
                return cached; // resources in cache
            }

            return fetch(event.request)
                .then(response => {

                    // dynamic caching of html pages in backend
                    if (
                        response.ok &&
                        response.headers.get('Content-Type')?.includes('text/html')
                    ) {
                        const copy = response.clone();
                        caches.open('html-pages').then(cache => {
                            cache.put('/', copy);
                            cache.put('/landing-page.html', copy);
                            cache.put(event.request, copy);
                        });
                    }

                    return response;
                })
                .catch(() => {
                    // fallback HTML offline
                    return caches.match('/offline.html');
                });
        })
    );
});
