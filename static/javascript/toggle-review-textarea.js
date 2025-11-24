// Show or hide the review form and the static view
function toggleEditor() {
  const form = document.querySelector('#recensione-form'); // select form
  const view = document.querySelector('#recensione-view'); // select review view
  $(form).toggle(); // show/hide form
  $(view).toggle(); // show/hide view
}

// Save the review via POST
function salvaRecensione(event) {
  event.preventDefault(); // prevent default submit behavior

  const textArea = document.querySelector('#textarea-recensione'); // review text
  const filmId   = document.querySelector('.recensione-personale-wrapper').dataset.filmId; // movie id

  // send the review to the server
  fetch(`/movie-card/${filmId}`, {
    method: "POST", // POST method
    body: new URLSearchParams({ recensione: textArea.value }), // data sent
    headers: { "Content-Type": "application/x-www-form-urlencoded" } // content type
  })
    .then(res => res.json()) // read JSON response
    .then(data => {
      if (data.success) {
        document.querySelector('#recensione-testo-statico').textContent = textArea.value; // update displayed text
        toggleEditor(); // hide form and show view
      } 
    });
}
