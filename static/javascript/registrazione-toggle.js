// Check if the registration form is visibile at the beginning
let isRegistrazioneVisibile = document.querySelector('#registration-form').classList.contains('active');

// toggle from registration to login form and viceversa
function toggleForms() {
    // toggle the visibility status 
    isRegistrazioneVisibile = !isRegistrazioneVisibile;

    const formRegistrazione = document.querySelector('#registration-form'); // registration form
    const loginForm         = document.querySelector('#login-form');        // login form

    if (isRegistrazioneVisibile) {
        // show registration and hide login
        formRegistrazione.classList.add('active');
        loginForm.classList.remove('active');
    } else {
        // show login, and hide registration
        formRegistrazione.classList.remove('active');
        loginForm.classList.add('active');
    }
}
