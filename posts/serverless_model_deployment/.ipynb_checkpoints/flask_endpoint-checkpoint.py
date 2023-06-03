from flask import Flask, request, jsonify
import cloudpickle

app = Flask(__name__)

# Load model once at startup
with open('model.pickle', 'rb') as f:
    model = cloudpickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        predictions = model.predict(data).tolist()
        return jsonify({'predictions': predictions})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run with `gunicorn -w 8 flask_endpoint:app` on the command line
if __name__ == "__main__":
    app.run(debug=False)
    
