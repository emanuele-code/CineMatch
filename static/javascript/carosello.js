document.addEventListener('DOMContentLoaded', () => {
  const slides     = document.querySelectorAll('.slider a');
  const navLinks   = document.querySelectorAll('.slider-nav a');
  let indiceAttuale = 0;

  function mostraSlide(index) {
    slides.forEach(slide => $(slide).hide());   
    $(slides[index]).show();                   
  }

  mostraSlide(indiceAttuale);

  // change slide every 5 seconds
  let intervallo = setInterval(() => {
    indiceAttuale = (indiceAttuale + 1) % slides.length;
    mostraSlide(indiceAttuale);
  }, 5000);

  // handle nav click
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
