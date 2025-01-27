// This script hides notification messages so they start to fade out after 8 seconds
// and will be removed from the DOM 1 second after they start fading out,
// ie. total = 9 seconds from the page load to the message removal.
function hideMessages() {
    setTimeout(function() {
        var messages = document.querySelectorAll('.alert');
        messages.forEach(function(msg) {
            msg.classList.remove('show');
            msg.classList.add('fade');
            // remove the message from the DOM after it fades out
            setTimeout(function() {
                msg.remove();
            }, 1000); // 1 second
        });
    }, 8000);
}

// Call the function to hide messages
document.addEventListener('DOMContentLoaded', function() {
    hideMessages();
});