document.addEventListener('DOMContentLoaded', () => {
  const starContainers = document.querySelectorAll('.interactive-stars');

  starContainers.forEach(container => {
    const stars = container.querySelectorAll('.star');
    const currentStars = parseInt(container.dataset.currentStars) || 0;

    function highlightStars(count) {
      stars.forEach((star, idx) => {
        if (idx < count) {
          star.classList.add('filled');
        } else {
          star.classList.remove('filled');
        }
      });
    }

    stars.forEach((star, idx) => {
      star.addEventListener('mouseover', () => {
        highlightStars(idx + 1);
      });

      star.addEventListener('mouseout', () => {
        highlightStars(currentStars);
      });

      star.addEventListener('click', () => {
        container.dataset.currentStars = idx + 1;
        highlightStars(idx + 1);
        // Qui potresti aggiungere anche una chiamata ajax per salvare il voto utente
      });
    });

    // Imposta la visualizzazione iniziale
    highlightStars(currentStars);
  });
});
