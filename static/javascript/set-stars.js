document.addEventListener('DOMContentLoaded', () => {
  // Seleziono tutti i contenitori di stelle interattive
  document.querySelectorAll('.interactive-stars').forEach(contenitore => {
    const filmId = contenitore.dataset.filmId; // prendo l'ID del film

    // Aggiungo l'evento click a ciascuna stella
    contenitore.querySelectorAll('.star').forEach(stella => {
      stella.addEventListener('click', () => {
        const voto = parseInt(stella.dataset.value); // leggo il valore della stella cliccata

        // Invio il voto al server via POST
        fetch('/aggiorna_voto', {
          method:      'POST',                       // metodo POST
          headers:     { 'Content-Type': 'application/json' }, // tipo di contenuto JSON
          credentials: 'include',                    // include cookie/sessione
          body:        JSON.stringify({ film_id: filmId, voto }) // corpo della richiesta
        });
      });
    });
  });
});
