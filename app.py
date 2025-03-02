# from flask import Flask, render_template, jsonify, request
# import RPi.GPIO as GPIO
# import time
# import threading

# app = Flask(__name__)

# # GPIO setup
# GPIO.setmode(GPIO.BCM)

# # Define GPIO pins
# devices = {
#     'fan': 17,  # Fan GPIO pin
#     'light': 27  # Light GPIO pin
# }
# ir_sensor = 22  # IR Sensor GPIO pin

# # Setup GPIO pins
# GPIO.setup(ir_sensor, GPIO.IN)  # IR sensor as input
# for device in devices.values():
#     GPIO.setup(device, GPIO.OUT)
#     GPIO.output(device, GPIO.LOW)  # Initially OFF

# # Device states
# device_states = {
#     'fan': False,
#     'light': False
# }

# # Function to monitor IR sensor
# def monitor_ir_sensor():
#     while True:
#         if GPIO.input(ir_sensor) == 1:  # Object detected
#             print("Motion detected! Turning ON devices.")
#             GPIO.output(devices['fan'], GPIO.HIGH)
#             GPIO.output(devices['light'], GPIO.HIGH)
#             device_states['fan'] = True
#             device_states['light'] = True
#         else:  # No object detected
#             print("No motion detected. Turning OFF devices.")
#             time.sleep(5400)  # Wait for 5 seconds before turning off
#             GPIO.output(devices['fan'], GPIO.LOW)
#             GPIO.output(devices['light'], GPIO.LOW)
#             device_states['fan'] = False
#             device_states['light'] = False
#         time.sleep(1)  # Polling interval

# # Start monitoring IR sensor in a separate thread
# threading.Thread(target=monitor_ir_sensor, daemon=True).start()

# @app.route('/')
# def home():
#     return render_template('index.html', devices=device_states)

# @app.route('/toggle_device', methods=['POST'])
# def toggle_device():
#     device = request.json['device']
#     state = request.json['state']
    
#     # Toggle GPIO state
#     GPIO.output(devices[device], GPIO.HIGH if state else GPIO.LOW)
#     device_states[device] = state

#     print(f"{device} turned {'ON' if state else 'OFF'} via web")

#     return jsonify(success=True, device_states=device_states)

# @app.route('/device_status', methods=['GET'])
# def device_status():
#     """ API to fetch real-time device status """
#     return jsonify(device_states)

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')


from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Simulated device states (instead of GPIO)
device_states = {
    'fan': False,
    'light': False
}

@app.route('/')
def home():
    return render_template('index.html', devices=device_states)

@app.route('/toggle_device', methods=['POST'])
def toggle_device():
    device = request.json['device']
    state = request.json['state']
    device_states[device] = state  # Update state in dictionary (no GPIO)
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
