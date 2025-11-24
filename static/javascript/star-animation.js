document.addEventListener('DOMContentLoaded', () => {
  // Select all star containers
  document.querySelectorAll('.interactive-stars').forEach(contenitore => {
    const stelle        = contenitore.querySelectorAll('.star'); // all stars in the container
    let   stelleAttuali = parseInt(contenitore.dataset.currentStars) || 0; // current rating
    const filmId        = contenitore.dataset.filmId; // movie ID

    // Function to highlight stars up to "count"
    function illuminaStelle(count) {
      stelle.forEach((stella, idx) => {
        stella.classList.toggle('filled', idx < count); // add/remove 'filled' class
      });
    }

    // Events for each star
    stelle.forEach((stella, idx) => {
      stella.addEventListener('mouseover', () => illuminaStelle(idx + 1)); // highlight on hover
      stella.addEventListener('mouseout',  () => illuminaStelle(stelleAttuali)); // restore current stars
      stella.addEventListener('click', () => {
        const voto    = idx + 1;
        stelleAttuali = voto;
        contenitore.dataset.stelleAttuali = voto; // update dataset
        illuminaStelle(voto); // highlight selected stars

        const statusDiv = document.querySelector(`#status-${filmId}`);

        // If rating > 0, update status to "watched"
        if (statusDiv && voto > 0) {
          statusDiv.innerHTML = 'Visto';
          statusDiv.className = 'movie-status visto';
        
          // send status update to server
          fetch('/aggiorna_stato', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            credentials: 'include',
            body: JSON.stringify({ film_id: filmId, stato: 'visto' })
          });
        }

        // send rating to the server
        fetch('/aggiorna_voto', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          credentials: 'include',
          body: JSON.stringify({ film_id: filmId, voto })
        });

      });
    });

    // Set initial display of stars
    illuminaStelle(stelleAttuali);
  });
});
