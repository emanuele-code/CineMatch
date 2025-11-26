const cacheName = 'pwaCinematch';

// lists of assests to cache
const cacheList = [
    '/', // L'indice della tua app (fondamentale per l'esperienza offline)
    'manifest.json',

    // css
    'static/css/style-landing-page.css',
    'static/css/style-lista.css',
    'static/css/style-logged-home-page.css',
    'static/css/style-movie-card.css',
    'static/css/style-registrazione.css',

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

    // html
    '/landing-page.html',
    '/lista.html',
    '/logged-home-page.html',
    '/movie-card.html',
    '/registrazione.html',

    // images
    '/static/images/clapperboard.jpg', //icona
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
    '/static/images/inglourious-basterds.jpg',
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

// 2. 'fetch': it cache first and then loadd the network 
self.addEventListener('fetch', e => {
    // intercept http request and it try to respond first from cache, if it miss it will try with network
    e.respondWith(
        caches.match(e.request)
            .then(cachedResponse => {
                // if the resource is in the cache it will be returned instantly
                return cachedResponse || fetch(e.request);
        })
    );
});