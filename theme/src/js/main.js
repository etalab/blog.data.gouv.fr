// Main menu dropdowns
[].forEach.call(document.querySelectorAll('li.dropdown'), function(dropdown) {
    dropdown.addEventListener('click', function() {
        dropdown.classList.toggle('open');
    })
});
