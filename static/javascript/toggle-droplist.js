function toggleDropdown(id) {
  const dropdown = document.getElementById('dropdown-' + id);
  dropdown.style.display = dropdown.style.display === 'none' ? 'block' : 'none';
}

function updateStatus(id, newStatus) {
  fetch(`/update-status/${id}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ stato: newStatus })
  })
  .then(response => {
    if (response.ok) {
      window.location.reload(); // Ricarica la pagina per riflettere le modifiche
    } else {
      alert("Errore durante l'aggiornamento dello stato");
    }
  });
}
