document.addEventListener('DOMContentLoaded', function() {
    // wait for the DOM to load before executing the code
    const editButtons = document.getElementsByClassName("btn-edit");
    const postTitle = document.getElementById("id_title");
    const postContent = document.getElementById("id_content");
    const postImage = document.getElementById("id_image");
    const postStatus = document.getElementById("id_status");
    const postForm = document.getElementById("postForm");
    const postFormTitle = document.getElementById("postFormTitle");
    const submitButton = document.getElementById("submitButton");

    // const updateButton = document.getElementById("updateButton");
    // const changeImageButton = document.getElementById("changeImageButton");
    // const imagePreviewContainer = document.getElementById("image-preview-container");

    let imageChanged = false;
    let currentImageUrl = '';

        /**
    * Initializes edit functionality for the provided edit buttons.
    * 
    * For each button in the `editButtons` collection:
    * - Retrieves the associated post's ID upon click.
    * - Fetches the content of the corresponding post.
    * - Populates the `postTitle`, `postContent` textbox and textarea with the post's content for editing.
    * - Hides submit button and displays update button.
    * - Sets the form's action attribute to the `edit_post/{postId}` endpoint.
    */
    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            let postId = e.target.getAttribute("data-post_id");
            let postElement = document.getElementById(`post${postId}`);
            if (postElement) {
                let title = postElement.getAttribute("data-title");
                let content = postElement.getAttribute("data-content");
                currentImageUrl = postElement.getAttribute("data-image-url");
                postFormTitle.innerText = "Edit Post Text";
                postTitle.value = title;
                postContent.value = content;
                postStatus.value = 0; // Set status to draft
                // Display the current image URL in an image preview container
                const imagePreviewContainer = document.getElementById("image-preview-container");
                if (imagePreviewContainer) {
                    imagePreviewContainer.innerHTML = `<img src="${currentImageUrl}" alt="Current Image" />`;
                    imagePreviewContainer.style.display = 'block';
                }
                if (postImage) {
                    postImage.value = ''; // Clear the file input
                    postImage.style.display = 'block'; // Show the image uploading widget
                    postImage.addEventListener('change', () => {
                        imageChanged = true; // Set the flag when the image is changed
                    });
                }
                const changeImageButton = document.getElementById("changeImageButton");
                if (changeImageButton) {
                    changeImageButton.style.display = 'block';
                }

                submitButton.innerText = 'Update';
                postForm.setAttribute("action", `edit_post/${postId}`);
                imageChanged = false; // Reset the flag
            } else {
                console.error(`Element with ID post${postId} not found.`);
            }
        });
    }

    postForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const formData = new FormData(postForm);
    
        if (!imageChanged) {
            formData.delete('image'); // Remove image field if not changed
            formData.append('image_url', currentImageUrl); // Add the existing image URL
        }
    
        fetch(postForm.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest', // Optional for Django AJAX detection
            },
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                window.location.reload(); // Reload on success
            } else {
                alert('Error: ' + JSON.stringify(data.errors));
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while updating the post.');
        });
    });
    
});