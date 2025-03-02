function toggleDevice(device) {
    const button = document.getElementById(`${device}-button`);
    const currentState = button.innerText === 'ON';
    const newState = !currentState;

    fetch('/toggle_device', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ device: device, state: newState })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            button.innerText = newState ? 'ON' : 'OFF';
        }
    });
}
