# Install dependencies
pip install --user -r requirements.txt

# Set environment variable for the model path if needed
export MODEL_PATH=./model.json

# Run the Flask application
python app.py &
