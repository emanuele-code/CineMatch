document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.slider a');
    let currentIndex = 0;
    
    function showSlide(index) {
      // Nascondi tutte le slide
      slides.forEach(slide => slide.style.display = 'none');
      // Mostra la slide corrente
      slides[index].style.display = 'block';
    }

    showSlide(currentIndex);

    setInterval(() => {
      currentIndex = (currentIndex + 1) % slides.length;
      showSlide(currentIndex);
    }, 5000); 
  });