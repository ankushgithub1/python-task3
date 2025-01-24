from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, Kubernetes!"

@app.route('/cpu')
def cpu_stress():
    # Simulate CPU load to test auto-scaling
    for _ in range(10**7):
        pass
    return "CPU Load Simulated"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

