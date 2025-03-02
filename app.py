# from flask import Flask, render_template, jsonify, request
# import RPi.GPIO as GPIO

# app = Flask(__name__)

# # GPIO setup
# GPIO.setmode(GPIO.BCM)
# devices = {
#     'fan': 17,  # GPIO pin for fan
#     'light': 27  # GPIO pin for light
# }
# for device in devices.values():
#     GPIO.setup(device, GPIO.OUT)
#     GPIO.output(device, GPIO.LOW)

# device_states = {
#     'fan': False,
#     'light': False
# }

# @app.route('/')
# def home():
#     return render_template('index.html', devices=device_states)

# @app.route('/toggle_device', methods=['POST'])
# def toggle_device():
#     device = request.json['device']
#     state = request.json['state']
#     GPIO.output(devices[device], GPIO.HIGH if state else GPIO.LOW)
#     device_states[device] = state
#     return jsonify(success=True)

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
