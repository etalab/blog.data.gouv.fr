// Main menu dropdowns
[].forEach.call(document.querySelectorAll('li.dropdown'), function(dropdown) {

    dropdown.addEventListener('mouseover', function() {
        dropdown.classList.add('open');
    })
    dropdown.addEventListener('mouseout', function() {
        dropdown.classList.remove('open');
    })
});
