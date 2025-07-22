document.addEventListener('DOMContentLoaded', () => {
  const statoFiltro = document.getElementById('statoFiltro');
  const stelleFiltro = document.getElementById('stelleFiltro');
  const genereFiltro = document.getElementById('genereFiltro');
  const cards = document.querySelectorAll('.movie-card');

  function filtra() {
    const statoVal = statoFiltro.value;
    const stelleVal = stelleFiltro.value;
    const genereVal = genereFiltro.value;

    cards.forEach(card => {
      const statoDiv   = card.querySelector('.movie-status');
      const stelleDiv  = card.querySelector('.interactive-stars');
      const genereText = card.querySelector('p:nth-of-type(3)')?.textContent || ''; // "Genere: Azione"

      const statoClass   = statoDiv?.className.split(' ').pop(); // es: "visto"
      const currentStars = parseInt(stelleDiv?.dataset.currentStars || 0);
      const genere       = genereText.toLowerCase().split(':')[1]?.trim() || '';

      const matchStato  = statoVal === 'tutti' || statoClass === statoVal;
      const matchStelle = stelleVal === 'tutte' || currentStars === parseInt(stelleVal);
      const matchGenere = genereVal === 'tutti' || genere === genereVal;

      if (matchStato && matchStelle && matchGenere) {
        card.style.display = '';
      } else {
        card.style.display = 'none';
      }
    });
  }

  statoFiltro.addEventListener('change',  filtra);
  stelleFiltro.addEventListener('change', filtra);
  genereFiltro.addEventListener('change', filtra);
});
