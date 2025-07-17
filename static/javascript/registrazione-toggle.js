let isRegistrationVisible = true;

function toggleForms() {
    isRegistrationVisible = !isRegistrationVisible;

    const formRegistrazione = document.getElementById('registration-form');
    const loginForm = document.getElementById('login-form');
    const toggleLink = document.querySelector('.toggle-link');

    if (isRegistrationVisible) {
        formRegistrazione.classList.add('active');
        loginForm.classList.remove('active');
    } else {
        formRegistrazione.classList.remove('active');
        loginForm.classList.add('active');
    }

    isRegistrazioneVisibile = !mostraLogin;
}
