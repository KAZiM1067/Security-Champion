document.addEventListener('DOMContentLoaded', () => {
    const slider = document.querySelector('.slider');
    const slides = document.querySelectorAll('.slide');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');

    if (!slider || slides.length === 0 || !prevBtn || !nextBtn) {
        console.error("Slider or buttons not found!");
        return; // Exit script if elements are missing
    }

    const slideWidth = slides[0].offsetWidth; // Get slide width dynamically
    const imagesToShow = 3; // Number of images visible at a time
    let currentIndex = imagesToShow; // Start at first real slide

    // Clone slides for seamless infinite loop
    const firstClones = Array.from(slides).slice(0, imagesToShow).map(slide => slide.cloneNode(true));
    const lastClones = Array.from(slides).slice(-imagesToShow).map(slide => slide.cloneNode(true));

    firstClones.forEach(clone => slider.appendChild(clone)); // Add clones at the end
    lastClones.reverse().forEach(clone => slider.prepend(clone)); // Add clones at the beginning

    const updatedSlides = document.querySelectorAll('.slide'); // Get updated slides

    // Set initial position
    slider.style.transform = `translateX(-${currentIndex * slideWidth}px)`;

    function updateSlider() {
        slider.style.transition = 'transform 0.5s ease-in-out';
        slider.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
    }

    //Next Button Click - Works Now!
    nextBtn.addEventListener('click', () => {
        console.log('Next button clicked');
        if (currentIndex >= updatedSlides.length - imagesToShow) return; // Prevent extra clicks
        currentIndex++;
        updateSlider();
    });

    //Previous Button Click - Works Now!
    prevBtn.addEventListener('click', () => {
        console.log('Prev button clicked');
        if (currentIndex <= 0) return; // Prevent extra clicks
        currentIndex--;
        updateSlider();
    });

    // Reset transition for infinite loop effect
    slider.addEventListener('transitionend', () => {
        if (currentIndex >= updatedSlides.length - imagesToShow) {
            slider.style.transition = 'none';
            currentIndex = imagesToShow;
            slider.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
        } else if (currentIndex < imagesToShow) {
            slider.style.transition = 'none';
            currentIndex = updatedSlides.length - imagesToShow - 1;
            slider.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
        }
    });

    // Resize Event (Recalculate Slide Width)
    window.addEventListener('resize', () => {
        const newSlideWidth = slides[0].offsetWidth;
        slider.style.transition = 'none';
        slider.style.transform = `translateX(-${currentIndex * newSlideWidth}px)`;
    });
});
