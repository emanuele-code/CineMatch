document.addEventListener('DOMContentLoaded', function () {
    const userDropdown  = document.querySelector('#userDropdown');
    const dropdownMenu  = document.querySelector('#dropdownMenu');

    userDropdown.addEventListener('click', function (e) {
        e.preventDefault();
        $(dropdownMenu).toggle();
    });

    document.addEventListener('click', function (e) {
        if (!userDropdown.contains(e.target) && !dropdownMenu.contains(e.target)) {
            $(dropdownMenu).hide();
        }
    });
});
