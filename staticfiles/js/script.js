document.addEventListener('DOMContentLoaded', function() {
    const postForm = document.getElementById('postForm');
    const imageInput = postForm.querySelector('input[type="file"]');
    const previewContainer = document.createElement('div');
    previewContainer.classList.add('image-preview-container');
    postForm.insertBefore(previewContainer, postForm.querySelector('button'));

    imageInput.addEventListener('change', function() {
        previewContainer.innerHTML = '';
        const file = imageInput.files[0];
        const reader = new FileReader();
        reader.onload = function(e) {
            const img = document.createElement('img');
            img.src = e.target.result;
            img.classList.add('image-preview');
            previewContainer.appendChild(img);
        };
        reader.readAsDataURL(file);
    });

    postForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(postForm);
        fetch(postForm.action, {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.reload();
            } else {
                alert('Error uploading images: ' + JSON.stringify(data.errors));
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error uploading images');
        });
    });
});