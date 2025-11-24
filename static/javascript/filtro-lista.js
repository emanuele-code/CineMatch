document.addEventListener('DOMContentLoaded', () => {
  // Select filters
  const statoFiltro  = document.querySelector('#statoFiltro');
  const stelleFiltro = document.querySelector('#stelleFiltro');
  const genereFiltro = document.querySelector('#genereFiltro');
  // Select every film card
  const carte        = document.querySelectorAll('.movie-card');

  // filter card function
  function filtra() {
    const statoVal  = statoFiltro.value;   // selected value of the status filter
    const stelleVal = stelleFiltro.value;  // selected value of the star filter
    const genereVal = genereFiltro.value;  // selected value of the genre filter

    carte.forEach(carta => {
      const statoDiv   = carta.querySelector('.movie-status');          // div film status
      const stelleDiv  = carta.querySelector('.interactive-stars');     // div film star
      const genereText = carta.querySelector('p:nth-of-type(3)')?.textContent || ''; // text genre

      const statoClass    = statoDiv?.className.split(' ').pop();                 // status class
      const stelleAttuali = parseInt(stelleDiv?.dataset.currentStars || 0);       // star number
      const genere        = genereText.toLowerCase().split(':')[1]?.trim() || ''; // trimmed text genre

      // check if the card match the filters
      const matchStato  = statoVal  === 'tutti' || statoClass === statoVal;
      const matchStelle = stelleVal === 'tutte' || stelleAttuali === parseInt(stelleVal);
      const matchGenere = genereVal === 'tutti' || genere === genereVal;

      // show/hide the card based on filters
      $(carta).toggle(matchStato && matchStelle && matchGenere);
    });
  }

  // Event listener on filters to apply changes
  statoFiltro.addEventListener('change',  filtra);
  stelleFiltro.addEventListener('change', filtra);
  genereFiltro.addEventListener('change', filtra);
});
