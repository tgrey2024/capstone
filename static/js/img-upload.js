document.addEventListener('DOMContentLoaded', () => {
    // Get the form element with the ID 'postForm'
    const postForm = document.getElementById('postForm');
    // Check if the form element exists
    if (!postForm) {
        console.error('postForm element not found');
        return; // Exit if the form is not found
    }

    // Get the file input element within the form
    const imageInput = postForm.querySelector('input[type="file"]');
    // Check if the file input element exists
    if (!imageInput) {
        console.error('File input element not found');
        return;
    }

    // Create a new div element with class 'image-preview-container' before the button element within the postForm
    // to serve as a container for image previews
    const previewContainer = document.createElement('div');
    previewContainer.classList.add('image-preview-container');
    postForm.insertBefore(previewContainer, postForm.querySelector('button'));

    // Listen for changes on an input element (image file input)
    // when file selected, reads the file
    // displays a preview of the image in a specified container. 
    imageInput.addEventListener('change', () => {
        previewContainer.innerHTML = '';
        const file = imageInput.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                const img = document.createElement('img');
                // Set the source of the image to the result of the FileReader
                img.src = e.target.result;
                img.classList.add('image-preview');
                previewContainer.appendChild(img);
            };
            reader.readAsDataURL(file);
        }
    });

    // submits the form data using an AJAX request, ensures user can see a preview of the selected image before submitting the form
    // handles any errors that may occur during the submission process
    // Add an event listener to the form for the 'submit' event
    postForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const formData = new FormData(postForm);
        // Send the form data using the Fetch API
        fetch(postForm.action, {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        
        .then(data => {
            if (data.success) { // If the response indicates success, reload the page
                window.location.reload();
            } else { // If there are errors, show an alert with the error messages
                alert('Error uploading images: ' + JSON.stringify(data.errors));
            }
        })
        .catch(error => { // If there is a network or other error, log it and show an alert
            console.error('Error:', error);
            alert('Error uploading images');
        });
    });
});