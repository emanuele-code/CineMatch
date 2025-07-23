function toggleEditor() {
  const form = document.getElementById('recensione-form');
  const view = document.getElementById('recensione-view');
  form.style.display = form.style.display === 'none' ? 'block' : 'none';
  view.style.display = view.style.display === 'none' ? 'block' : 'none';
}




function salvaRecensione(event) {
  event.preventDefault();

  const form = document.getElementById("recensione-form");
  const textarea = document.getElementById("textarea-recensione");
  const filmId = document.querySelector(".recensione-personale-wrapper").dataset.filmId;

  fetch(`/movie-card/${filmId}`, {
    method: "POST",
    body: new URLSearchParams({ recensione: textarea.value }),
    headers: {
      "Content-Type": "application/x-www-form-urlencoded"
    }
  })
    .then(res => res.json())
    .then(data => {
      if (data.success) {
        document.getElementById("recensione-testo-statico").textContent = textarea.value;
        toggleEditor();
      } else {
        alert("Errore: " + (data.error || "impossibile salvare"));
      }
    });
}

