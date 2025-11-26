// BOM event when the page is fully loaded 
window.onload() = () => {
    'use strict'; // js strict mode, used to stop the program and avoid error beforehand

    // the navigator object container browser information, so in the if statment we are cheking for compatibility
    if('serviceWorker' in navigator) {
        // it will send the instruction to download and execute the serviceWorker sw.js
        navigator.serviceWorker.register('./sw.js')
            .then(registration => {
                console.log('Service Worker registrato');
            }).catch(error => {
                console.log('Errore nella registrazione del service worker', error);
            })
    }

}