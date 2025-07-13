let isRegistrationVisible = true;

function toggleForms() {
    isRegistrationVisible = !isRegistrationVisible;

    const registrationForm = document.getElementById('registration-form');
    const loginForm = document.getElementById('login-form');
    const toggleLink = document.querySelector('.toggle-link');

    if (isRegistrationVisible) {
        registrationForm.classList.add('active');
        loginForm.classList.remove('active');
    } else {
        registrationForm.classList.remove('active');
        loginForm.classList.add('active');
    }
}
