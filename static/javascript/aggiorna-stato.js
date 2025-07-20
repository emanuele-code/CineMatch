
function updateStatus(film_id, stato) {
  fetch('/aggiorna_stato', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    credentials: 'include',
    body: JSON.stringify({ film_id, stato })
  })
  .then(res => res.json())
  .then(data => {
    if (data.success) {
      // Aggiorna UI (testuale + classe)
      const statusDiv = document.querySelector(`.movie-status`);
      if (stato === 'visto') {
        statusDiv.textContent = '👁️ Visto';
        statusDiv.className = 'movie-status visto';
      } else if (stato === 'da vedere') {
        statusDiv.textContent = '🎯 Da vedere';
        statusDiv.className = 'movie-status da-vedere';
      } else {
        statusDiv.textContent = '➕ Imposta stato';
        statusDiv.className = 'movie-status nessuno';
      }

      // Chiudi dropdown
      document.getElementById(`dropdown-${film_id}`).style.display = 'none';
    } else {
      alert('Errore nell\'aggiornamento dello stato');
    }
  });
}
