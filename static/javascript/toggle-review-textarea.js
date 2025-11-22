// Mostra o nasconde il form di recensione e la visualizzazione statica
function toggleEditor() {
  const form = document.querySelector('#recensione-form'); // seleziona form
  const view = document.querySelector('#recensione-view'); // seleziona visualizzazione recensione
  $(form).toggle(); // mostra/nascondi form
  $(view).toggle(); // mostra/nascondi visualizzazione
}

// Salva la recensione tramite POST
function salvaRecensione(event) {
  event.preventDefault(); // evita il comportamento di submit predefinito

  const textArea = document.querySelector('#textarea-recensione'); // testo della recensione
  const filmId   = document.querySelector('.recensione-personale-wrapper').dataset.filmId; // id del film

  // invia la recensione al server
  fetch(`/movie-card/${filmId}`, {
    method: "POST", // metodo POST
    body: new URLSearchParams({ recensione: textArea.value }), // dati inviati
    headers: { "Content-Type": "application/x-www-form-urlencoded" } // tipo di contenuto
  })
    .then(res => res.json()) // legge la risposta JSON
    .then(data => {
      if (data.success) {
        document.querySelector('#recensione-testo-statico').textContent = textArea.value; // aggiorna testo visualizzato
        toggleEditor(); // nasconde il form e mostra la visualizzazione
      } 
    });
}
