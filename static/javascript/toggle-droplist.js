// Mostra o nasconde il dropdown corrispondente
function toggleDropdown(id) {
  const dropdown = document.querySelector('#dropdown-' + id); // seleziona dropdown
  $(dropdown).toggle();                                       // mostra/nascondi con jQuery
}

// Aggiorna lo stato di un film
function aggiornaStato(id, nuovoStato) {
  fetch(`/update-status/${id}`, {
    method: 'POST',                                  // metodo POST
    headers: { 'Content-Type': 'application/json' }, // tipo di contenuto JSON
    body: JSON.stringify({ stato: nuovoStato })      // dati inviati
  })
  .then(response => response.json())                 // leggi la risposta JSON
  .then(data => {
    if (data.success) {
      const divStato = document.querySelector(`#status-${id}`); // seleziona div stato
      if (divStato) {
        divStato.textContent = nuovoStato;          // aggiorna testo
        divStato.className   = 'movie-status ' + nuovoStato.toLowerCase(); // aggiorna classe
      }
    }
  });
}
