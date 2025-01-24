document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM loaded");
    var fileInputs = document.querySelectorAll('input[type="file"]');
    console.log(fileInputs);
    fileInputs.forEach(function(input) {
        input.addEventListener('change', function() {
            var label = input.nextElementSibling;
            if (input.files.length > 0) {
                label.textContent = input.files[0].name;
            } else {
                console.log(input.getAttribute('data-browse'));
                label.textContent = input.getAttribute('data-browse');
            }
        });
    });
});