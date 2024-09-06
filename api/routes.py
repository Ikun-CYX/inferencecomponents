from api import app
from flask import jsonify, request
from api.inference import Inference_Component
from api.record import Receive_Feedback

@app.route('/gameInference')
def index():
    return 'Hello! This is an inference prediction plug-in for making slot game.'


@app.route('/gameInference/nextComponent', methods=['POST'])
def nextComponent():
    if request.is_json:
        data = request.get_json()
        Next_Component = Inference_Component(data["Components"])
        return jsonify({"Next_Component": Next_Component}), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400

@app.route('/gameInference/recordFeedback', methods=['POST'])
def recordFeedback():
    if request.is_json:
        data = request.get_json()
        Receive_Feedback(data)
        return jsonify({"message": "Feedback received, thank you"}), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400