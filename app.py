from flask import Flask, request, jsonify
from model import ModelWrapper

app = Flask(__name__)
model_wrapper = ModelWrapper()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model_wrapper.predict(data['features'])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)