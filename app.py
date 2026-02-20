from flask import Flask, render_template, request, jsonify
from simulation_engine import run_simulation, load_module, load_presets

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.get_json()
    result = run_simulation(data)
    return jsonify(result)

@app.route('/load_module', methods=['POST'])
def module():
    data = request.get_json()
    return jsonify(load_module(data["name"]))

@app.route('/presets')
def presets():
    return jsonify(load_presets())

if __name__ == '__main__':
    app.run(debug=True)
