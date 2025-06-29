document.addEventListener('DOMContentLoaded', function() {
    const urlParams = new URLSearchParams(window.location.search);
    const message = urlParams.get('message');

    if (message === 'signup-success') {
        const messageDiv = document.getElementById('login-message');
        messageDiv.innerText = 'Sign up successful! Please log in.';
        messageDiv.style.display = 'block';
    }
});

document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const loginMessageDiv = document.getElementById('login-message');
    const storedEmail = localStorage.getItem('userEmail');
    const storedPassword = localStorage.getItem('userPassword');

    if (email === storedEmail && password === storedPassword) {
        loginMessageDiv.innerText = 'Login successful!';
        loginMessageDiv.style.color = 'green';
        loginMessageDiv.style.display = 'block';
        // Redirect to dashboard or home page
    } else {
        loginMessageDiv.innerText = 'Login failed. Please try again.';
        loginMessageDiv.style.color = 'red';
        loginMessageDiv.style.display = 'block';
    }
});