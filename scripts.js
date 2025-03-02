function toggleDevice(device) {
    const button = document.getElementById(`${device}-button`);
    const currentState = button.innerText === 'ON';
    const newState = !currentState;

    // Immediately update UI (Optimistic Update)
    button.innerText = newState ? 'ON' : 'OFF';
    button.style.backgroundColor = newState ? 'green' : 'red';

    fetch('/toggle_device', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ device: device, state: newState })
    })
    .then(response => response.json())
    .then(data => {
        if (!data.success) {
            // If the request fails, revert the UI changes
            button.innerText = currentState ? 'ON' : 'OFF';
            button.style.backgroundColor = currentState ? 'green' : 'red';
        }
    })
    .catch(() => {
        // Handle network error: revert UI changes
        button.innerText = currentState ? 'ON' : 'OFF';
        button.style.backgroundColor = currentState ? 'green' : 'red';
    });
}

// Fetch device status every 2 seconds to sync with hardware
function fetchDeviceStatus() {
    fetch('/device_status')
    .then(response => response.json())
    .then(data => {
        updateDeviceButtons(data);
    });
}

function updateDeviceButtons(deviceStates) {
    for (const [device, state] of Object.entries(deviceStates)) {
        const button = document.getElementById(`${device}-button`);
        button.innerText = state ? 'ON' : 'OFF';
        button.style.backgroundColor = state ? 'green' : 'red';
    }
}

setInterval(fetchDeviceStatus, 2000);  // Keep UI synced
