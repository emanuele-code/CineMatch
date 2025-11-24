function aggiornaStato(film_id, stato) {
  const divStato          = document.querySelector(`#status-${film_id}`);
  const contenitoreStelle = document.querySelector(`.interactive-stars[data-film-id="${film_id}"]`);

  let voto = 0; // default

  if (divStato) {
    if (stato === 'visto') {
      divStato.innerHTML = 'Visto';
      divStato.className = 'movie-status visto';
      if (contenitoreStelle) {
        voto = parseInt(contenitoreStelle.dataset.stelleAttuali) || 0;
      }
    } else if (stato === 'da vedere') {
      divStato.innerHTML = 'Da vedere';
      divStato.className = 'movie-status da-vedere';
      // do not touch the stars
      if (contenitoreStelle) {
        voto = 0; 
      }
    } else { // nessuno
      divStato.innerHTML = 'Imposta stato';
      divStato.className = 'movie-status nessuno';
      voto = 0; 
    }
  }

  // Update the stars in the DOM
  if (contenitoreStelle) {
    contenitoreStelle.dataset.stelleAttuali = voto;
    contenitoreStelle.querySelectorAll('.star').forEach((stella, idx) => {
      stella.classList.toggle('filled', idx < voto);
    });
  }

  // Close dropdown
  const dropdown = document.querySelector(`#dropdown-${film_id}`);
  if (dropdown) $(dropdown).hide();

  // Update status on the server
  fetch('/aggiorna_stato', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    credentials: 'include',
    body: JSON.stringify({ film_id, stato })
  });

  // Update rating on the server
  fetch('/aggiorna_voto', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    credentials: 'include',
    body: JSON.stringify({ film_id, voto })
  });
}
