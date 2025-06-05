const API_BASE = "http://127.0.0.1:8009";  // Your FastAPI backend URL

// Register
document.getElementById('registerForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const name = document.getElementById('reg_name').value.trim();
    const age = parseInt(document.getElementById('reg_age').value);
    const height = parseFloat(document.getElementById('reg_height').value);
    const weight = parseFloat(document.getElementById('reg_weight').value);

    if (!name || isNaN(age) || isNaN(height) || isNaN(weight)) {
        alert("Please fill all fields correctly.");
        return;
    }

    try {
        const response = await fetch(`${API_BASE}/users/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, age, height, weight }),
        });

        if (!response.ok) {
            throw new Error("Registration failed.");
        }

        const data = await response.json();
        alert(`Registered successfully! Your ID: ${data.id}`);
    } catch (error) {
        alert(`Error: ${error.message}`);
    }
});

// Login
document.getElementById('loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const name = document.getElementById('login_name').value.trim();

    if (!name) {
        alert("Please enter your name.");
        return;
    }

    try {
        const response = await fetch(`${API_BASE}/users/`);
        if (!response.ok) {
            throw new Error("Failed to fetch users.");
        }
        
        const users = await response.json();
        const user = users.find(u => u.name === name);

        if (user) {
            alert(`Login successful! Welcome, ${user.name}`);
            localStorage.setItem('userId', user.id);
            window.location.href = "dashboard.html";
        } else {
            alert('Invalid name!');
        }
    } catch (error) {
        alert(`Error: ${error.message}`);
    }
});
