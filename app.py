from flask import Flask, request, jsonify
from model import ModelWrapper
from model import RequestData
from model import RequestData

app = Flask(__name__)
model_wrapper = ModelWrapper()

@app.route('/predict', methods=['POST'])
def predict():
        json_data = request.get_json(force=True)
        request_data = RequestData(user_name=json_data['user_name'], age=json_data['age'], country=json_data['country'])
        request_data.validate()
        prediction = model_wrapper.predict(json_data['features'])
        return jsonify({'prediction': prediction})
        return jsonify({'error': 'Bad request', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)