document.addEventListener('DOMContentLoaded', function() {
    // wait for the DOM to load before executing the code
    const editButtons = document.getElementsByClassName("btn-edit");
    const postTitle = document.getElementById("id_title");
    const postContent = document.getElementById("id_content");
    const postImage = document.getElementById("id_image");
    const postStatus = document.getElementById("id_status");
    const postForm = document.getElementById("postForm");
    const submitButton = document.getElementById("submitButton");
    const changeImageButton = document.getElementById("changeImageButton");
    const imagePreviewContainer = document.getElementById("image-preview-container");

    let imageChanged = false;
    let currentImageUrl = '';

    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            let postId = e.target.getAttribute("data-post_id");
            let postElement = document.getElementById(`post${postId}`);
            if (postElement) {
                let title = postElement.getAttribute("data-title");
                let content = postElement.getAttribute("data-content");
                currentImageUrl = postElement.getAttribute("data-image-url");

                postTitle.value = title;
                postContent.value = content;
                postStatus.value = 0; // Set status to draft
                
                // Hide the image preview container and the image uploading widget
                imagePreviewContainer.style.display = 'none';
                postImage.style.display = 'none';
                changeImageButton.style.display = 'none';

                submitButton.innerText = "Update";
                postForm.setAttribute("action", `edit_post/${postId}`);
                imageChanged = false; // Reset the flag
            } else {
                console.error(`Element with ID post${postId} not found.`);
            }
        });
    }

    changeImageButton.addEventListener("click", () => {
        const existingPreview = document.querySelector('.image-preview');
        if (existingPreview) {
            existingPreview.remove();
        }
        postImage.style.display = 'block';
        changeImageButton.style.display = 'none';
        imageChanged = true; // Set the flag to indicate the image has been changed
    });

    postForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const formData = new FormData(postForm);

        if (!imageChanged) {
            // Remove the image field from the form data if the image has not been changed
            formData.delete('image');
            // Add the current image URL to the form data
            for (let [key, value] of formData.entries()) {
                console.log(`${key}: ${value}`);
            }
            formData.append('image_url', currentImageUrl);
        }

        fetch(postForm.action, {
            method: 'POST',
            body: formData,
        })
        .then(response => {
            console.log(response);
            console.log(response.json());
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
            if (data.success) {
                window.location.reload();
            } else {
                alert('Error updating post: ' + JSON.stringify(data.errors));
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error updating post: ' + error.message);
        });
    });
});