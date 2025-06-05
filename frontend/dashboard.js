const API_BASE = "http://127.0.0.1:8009";  // Backend URL

// Fetch userId from localStorage
const userId = localStorage.getItem('userId');

// If no userId found, redirect to login page
if (!userId) {
    alert('No user logged in! Redirecting to login...');
    window.location.href = 'index.html';
}

// Load Fitness Records
async function fetchRecords() {
    try {
        const response = await fetch(`${API_BASE}/users/${userId}/fitness_records/`);
        const records = await response.json();
        
        const fitnessList = document.getElementById('fitnessList');
        fitnessList.innerHTML = '';
        records.forEach(record => {
            const li = document.createElement('li');
            li.textContent = `Workout: ${record.workout_type}, Duration: ${record.duration_minutes} min`;
            fitnessList.appendChild(li);
        });
    } catch (error) {
        console.error('Fetch Records Error:', error);
        alert('Failed to load fitness records!');
    }
}

// Add New Fitness Record
document.getElementById('fitnessForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const workoutType = document.getElementById('workout_type').value;
    const durationMinutes = document.getElementById('duration_minutes').value;

    try {
        const response = await fetch(`${API_BASE}/users/${userId}/fitness_records/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                workout_type: workoutType,
                duration_minutes: parseInt(durationMinutes),
            }),
        });

        if (!response.ok) {
            throw new Error('Failed to add record');
        }

        const data = await response.json();
        alert(`Record added: ${data.workout_type}`);
        fetchRecords();  // Refresh records list
    } catch (error) {
        console.error('Add Record Error:', error);
        alert('Failed to add fitness record!');
    }
});

// Predict Calories
document.getElementById('predictForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const days = document.getElementById('days').value;

    try {
        const response = await fetch(`${API_BASE}/predict_calories/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ days: parseInt(days) }),
        });

        if (!response.ok) {
            throw new Error('Prediction failed');
        }

        const data = await response.json();
        document.getElementById('predictionResult').innerText = `Predicted Calories: ${data.predicted_calories}`;
    } catch (error) {
        console.error('Prediction Error:', error);
        alert('Failed to predict calories!');
    }
});
