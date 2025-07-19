document.querySelectorAll('.interactive-stars').forEach(container => {
  container.querySelectorAll('.star').forEach(star => {
    star.addEventListener('click', () => {
      const voto = parseInt(star.dataset.value);
      const film_id = container.dataset.filmId;

      container.querySelectorAll('.star').forEach(s => {
        const val = parseInt(s.dataset.value);
        s.classList.toggle('filled', val <= voto);
      });

      // Rimanda il fetch per dare tempo al browser di aggiornare la UI
      setTimeout(() => {
        fetch('/aggiorna_voto', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          credentials: 'include',
          body: JSON.stringify({ film_id, voto })
        })
        .then(response => response.json())
        .then(data => {
          if (!data.success) {
            alert('Errore nel salvataggio del voto.');
          }
        });
      }, 0);
    });
  });
});
