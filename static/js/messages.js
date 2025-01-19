function hideMessages() {
    setTimeout(function() {
        var messages = document.querySelectorAll('.alert');
        messages.forEach(function(msg) {
            msg.classList.remove('show');
            msg.classList.add('fade');
        });
    }, 15000);
}

// Call the function to hide messages
hideMessages();