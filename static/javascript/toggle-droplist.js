// Show or hide the corresponding dropdown
function toggleDropdown(id) {
  const dropdown = document.querySelector('#dropdown-' + id); // select dropdown
  $(dropdown).toggle();                                       // show/hide with jQuery
}

// Update the status of a movie
function aggiornaStato(id, nuovoStato) {
  fetch(`/update-status/${id}`, {
    method: 'POST',                                  // POST method
    headers: { 'Content-Type': 'application/json' }, // JSON content type
    body: JSON.stringify({ stato: nuovoStato })      // data sent
  })
  .then(response => response.json())                 // read JSON response
  .then(data => {
    if (data.success) {
      const divStato = document.querySelector(`#status-${id}`); // select status div
      if (divStato) {
        divStato.textContent = nuovoStato;          // update text
        divStato.className   = 'movie-status ' + nuovoStato.toLowerCase(); // update class
      }
    }
  });
}
