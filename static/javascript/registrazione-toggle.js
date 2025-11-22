// Controlla se il form di registrazione è visibile all'inizio
let isRegistrazioneVisibile = document.querySelector('#registration-form').classList.contains('active');

// Funzione per alternare tra form registrazione e login
function toggleForms() {
    // Invertiamo lo stato di visibilità del form di registrazione
    isRegistrazioneVisibile = !isRegistrazioneVisibile;

    const formRegistrazione = document.querySelector('#registration-form'); // form registrazione
    const loginForm         = document.querySelector('#login-form');        // form login

    if (isRegistrazioneVisibile) {
        // Mostra registrazione, nascondi login
        formRegistrazione.classList.add('active');
        loginForm.classList.remove('active');
    } else {
        // Mostra login, nascondi registrazione
        formRegistrazione.classList.remove('active');
        loginForm.classList.add('active');
    }
}
