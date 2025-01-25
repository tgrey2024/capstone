// This script is used to preview the image that the user has selected to upload
// as the cover image for their scrapbook or post.
document.addEventListener('DOMContentLoaded', function() {
    // if there is already an img element on the page
    // add an id of 'current-image-preview' to it
    // so that it can be removed if the user selects a new image
    const existingImg = document.querySelector('.current-image img');
    if (existingImg) {
        existingImg.id = 'current-image-preview';
    }
    // Add an event listener to the image input field    
    const imageInput = document.getElementById('id_image');
    if (imageInput) {
        imageInput.addEventListener('change', function(event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const imgContainer = document.querySelector('.current-image');
                    const img = document.getElementById('current-image-preview');
                    // If an image preview already exists, remove it
                    if (img) {
                        img.remove();
                    }
                    // Create a new image element and set its attributes
                    const newImg = document.createElement('img');
                    newImg.id = 'current-image-preview';
                    newImg.src = e.target.result;
                    newImg.alt = 'Thumbnail preview of Scrapbook Cover Image';
                    newImg.style.maxWidth = '200px';
                    newImg.style.marginTop = '10px';
                    newImg.style.marginBottom = '10px';
                    imgContainer.appendChild(newImg);
                };
                reader.readAsDataURL(file);
            }
        });
    }
});