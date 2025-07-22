document.addEventListener('DOMContentLoaded', () => {
  function aggiornaStelle(container, voto) {
    container.querySelectorAll('.star').forEach(star => {
      const val = parseInt(star.dataset.value);
      star.classList.remove('filled');
      if (val <= voto) {
        star.classList.add('filled');
      }
    });
    container.dataset.currentStars = voto;
  }

  document.querySelectorAll('.interactive-stars').forEach(container => {
    const filmId = container.dataset.filmId;

    // Invia il voto via POST e aggiorna direttamente le stelle
    container.querySelectorAll('.star').forEach(star => {
      star.addEventListener('click', () => {
        const voto = parseInt(star.dataset.value);

        fetch('/aggiorna_voto', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          credentials: 'include',
          body: JSON.stringify({ film_id: filmId, voto })
        })
        .then(response => {
          if (response.ok) {
            window.location.reload(); // Ricarica la pagina per riflettere le modifiche
          } else {
            alert("Errore durante l'aggiornamento dello stato");
          }
        });
      });
    });
  });
});
