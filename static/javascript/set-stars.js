document.querySelectorAll('.interactive-stars').forEach(starsContainer => {
  const filmId = starsContainer.dataset.filmId;
  let currentStars = parseInt(starsContainer.dataset.currentStars, 10);

  const stars = starsContainer.querySelectorAll('.star');

  // All'inizio colora le stelle in base al voto corrente
  updateStarsDisplay(currentStars);

  stars.forEach((star, index) => {
    star.addEventListener('click', () => {
      const selectedStars = index + 1;
      // Aggiorna nel backend
      fetch(`/modifica-stelle/${filmId}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ stelle: selectedStars }),
      })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          currentStars = selectedStars;
          updateStarsDisplay(currentStars);
        } else {
          alert('Errore: ' + data.error);
        }
      })
      .catch(() => alert('Errore di rete'));
    });
  });

  function updateStarsDisplay(starsCount) {
    stars.forEach((star, index) => {
      if (index < starsCount) {
        star.classList.add('filled');
      } else {
        star.classList.remove('filled');
      }
    });
  }
});
