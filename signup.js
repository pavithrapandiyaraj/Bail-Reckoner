document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    const role = document.getElementById('role').value;
    const signupMessageDiv = document.getElementById('signup-message');

    if (password !== confirmPassword) {
        signupMessageDiv.innerText = 'Passwords do not match. Please try again.';
        signupMessageDiv.style.display = 'block';
        return;
    }

    localStorage.setItem('userName', name);
    localStorage.setItem('userEmail', email);
    localStorage.setItem('userPassword', password);
    localStorage.setItem('userRole', role);

    window.location.href = `login.html?message=signup-success`;
});