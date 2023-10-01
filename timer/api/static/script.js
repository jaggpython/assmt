const images = document.querySelectorAll('.image-rotator img');
let currentIndex = 0;

function rotateImages() {
    images[currentIndex].style.opacity = 0;
    currentIndex = (currentIndex + 1) % images.length;
    images[currentIndex].style.opacity = 1;
}

setInterval(rotateImages, 2000); // Rotate images every 2 seconds
