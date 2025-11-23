document.addEventListener('DOMContentLoaded', () => {
  // Seleziono i filtri
  const statoFiltro  = document.querySelector('#statoFiltro');
  const stelleFiltro = document.querySelector('#stelleFiltro');
  const genereFiltro = document.querySelector('#genereFiltro');
  // Seleziono tutte le card dei film
  const carte        = document.querySelectorAll('.movie-card');

  // Funzione per filtrare le card
  function filtra() {
    const statoVal  = statoFiltro.value;   // valore selezionato del filtro stato
    const stelleVal = stelleFiltro.value;  // valore selezionato del filtro stelle
    const genereVal = genereFiltro.value;  // valore selezionato del filtro genere

    carte.forEach(carta => {
      const statoDiv   = carta.querySelector('.movie-status');          // div stato del film
      const stelleDiv  = carta.querySelector('.interactive-stars');    // div stelle del film
      const genereText = carta.querySelector('p:nth-of-type(3)')?.textContent || ''; // testo genere

      const statoClass    = statoDiv?.className.split(' ').pop();       // classe stato
      const stelleAttuali = parseInt(stelleDiv?.dataset.currentStars || 0); // numero stelle
      const genere        = genereText.toLowerCase().split(':')[1]?.trim() || ''; // testo genere pulito

      // verifico se la card corrisponde ai filtri
      const matchStato  = statoVal  === 'tutti' || statoClass === statoVal;
      const matchStelle = stelleVal === 'tutte' || stelleAttuali === parseInt(stelleVal);
      const matchGenere = genereVal === 'tutti' || genere === genereVal;

      // mostro/nascondo la card in base ai filtri
      $(carta).toggle(matchStato && matchStelle && matchGenere);
    });
  }

  // Event listener sui filtri per applicare il filtro al cambiamento
  statoFiltro.addEventListener('change',  filtra);
  stelleFiltro.addEventListener('change', filtra);
  genereFiltro.addEventListener('change', filtra);
});
