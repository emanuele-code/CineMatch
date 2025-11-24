document.addEventListener('DOMContentLoaded', () => {
  // Select every interactive star container
  document.querySelectorAll('.interactive-stars').forEach(contenitore => {
    const filmId = contenitore.dataset.filmId; // get film ID

    // add click event handler to each star
    contenitore.querySelectorAll('.star').forEach(stella => {
      stella.addEventListener('click', () => {
        const voto = parseInt(stella.dataset.value); // read the value of the clicked star

        // send the value to the server 
        fetch('/aggiorna_voto', {
          method:      'POST',                       
          headers:     { 'Content-Type': 'application/json' },   // type of content JSON
          credentials: 'include',                                // include cookie/session
          body:        JSON.stringify({ film_id: filmId, voto }) // request body
        });
      });
    });
  });
});
