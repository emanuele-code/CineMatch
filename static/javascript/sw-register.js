// BOM event when the page is fully loaded
window.onload = () => {

    // Verifica se il browser supporta i service worker
    if ('serviceWorker' in navigator) {

        // Ottieni tutte le registrazioni dei service worker
        navigator.serviceWorker.getRegistrations().then(registrations => {

            // Se non ci sono registrazioni, registriamo il service worker
            if (registrations.length === 0) {
                // Registriamo un nuovo service worker
                navigator.serviceWorker.register('/sw.js')
                    .then(registration => {
                        console.log('Service Worker registrato');
                    })
                    .catch(error => {
                        console.log('Errore nella registrazione del service worker', error);
                    });
            } else {
                // Se ci sono già registrazioni, non registriamo un altro service worker
                console.log('Service Worker già registrato');
            }
        }).catch(error => {
            console.log('Errore nel recupero delle registrazioni dei service worker', error);
        });
    }
}
