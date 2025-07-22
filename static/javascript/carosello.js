document.addEventListener('DOMContentLoaded', () => {
  const slides = document.querySelectorAll('.slider a');
  const navLinks = document.querySelectorAll('.slider-nav a');
  let currentIndex = 0;

  function showSlide(index) {
    slides.forEach(slide => slide.style.display = 'none');
    slides[index].style.display = 'block';
  }

  showSlide(currentIndex);

  // Cambia slide ogni 5 secondi
  let interval = setInterval(() => {
    currentIndex = (currentIndex + 1) % slides.length;
    showSlide(currentIndex);
  }, 5000);

  // Gestisci click sulle nav
  navLinks.forEach((link, index) => {
    link.addEventListener('click', e => {
      e.preventDefault(); // Previeni scroll con ancore
      currentIndex = index;
      showSlide(currentIndex);

      // resetta timer se vuoi
      clearInterval(interval);
      interval = setInterval(() => {
        currentIndex = (currentIndex + 1) % slides.length;
        showSlide(currentIndex);
      }, 5000);
    });
  });
});
