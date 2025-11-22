document.addEventListener('DOMContentLoaded', () => {
  // Seleziona tutti i contenitori delle stelle
  document.querySelectorAll('.interactive-stars').forEach(contenitore => {
    const stelle        = contenitore.querySelectorAll('.star'); // tutte le stelle nel contenitore
    let   stelleAttuali = parseInt(contenitore.dataset.stelleAttuali) || 0; // voto corrente
    const filmId        = contenitore.dataset.filmId; // ID del film

    // Funzione per evidenziare le stelle fino a "count"
    function illuminaStelle(count) {
      stelle.forEach((stella, idx) => {
        stella.classList.toggle('filled', idx < count); // aggiunge/rimuove classe 'filled'
      });
    }

    // Eventi per ogni stella
    stelle.forEach((stella, idx) => {
      stella.addEventListener('mouseover', () => illuminaStelle(idx + 1)); // evidenzia al passaggio
      stella.addEventListener('mouseout',  () => illuminaStelle(stelleAttuali)); // ripristina stelle correnti
      stella.addEventListener('click', () => {
        const voto    = idx + 1;
        stelleAttuali = voto;
        contenitore.dataset.stelleAttuali = voto; // aggiorna dataset
        illuminaStelle(voto); // evidenzia stelle selezionate

        const statusDiv = document.querySelector(`#status-${filmId}`);

        // Se voto > 0, aggiorna lo stato a "visto"
        if (statusDiv && voto > 0) {
          statusDiv.innerHTML = 'Visto';
          statusDiv.className = 'movie-status visto';
        
          // invia aggiornamento stato al server
          fetch('/aggiorna_stato', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            credentials: 'include',
            body: JSON.stringify({ film_id: filmId, stato: 'visto' })
          });
        }

        // invia il voto al server
        fetch('/aggiorna_voto', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          credentials: 'include',
          body: JSON.stringify({ film_id: filmId, voto })
        });

      });
    });

    // Imposta la visualizzazione iniziale delle stelle
    illuminaStelle(stelleAttuali);
  });
});
