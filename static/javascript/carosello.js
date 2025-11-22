document.addEventListener('DOMContentLoaded', () => {
  const slides     = document.querySelectorAll('.slider a');
  const navLinks   = document.querySelectorAll('.slider-nav a');
  let indiceAttuale = 0;

  function mostraSlide(index) {
    slides.forEach(slide => $(slide).hide());   
    $(slides[index]).show();                   
  }

  mostraSlide(indiceAttuale);

  // cambia slide ogni 5 secondi
  let intervallo = setInterval(() => {
    indiceAttuale = (indiceAttuale + 1) % slides.length;
    mostraSlide(indiceAttuale);
  }, 5000);

  // gestisci i click sul nav
  navLinks.forEach((link, index) => {
    link.addEventListener('click', e => {
      e.preventDefault(); 
      indiceAttuale = index;
      mostraSlide(indiceAttuale);

      // reset timer 
      clearInterval(intervallo);
      intervallo = setInterval(() => {
        indiceAttuale = (indiceAttuale + 1) % slides.length;
        mostraSlide(indiceAttuale);
      }, 5000);
    });
  });
});
