from flask import Flask, request, jsonify
import pickle
from sklearn.exceptions import NotFittedError

app = Flask(__name__)

# Load your model at startup
try:
    with open('model.pickle', 'rb') as f:
        model = pickle.load(f)
except (OSError, IOError) as e:
    print(f"Error: {e}")
    model = None

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        predictions = model.predict(data).tolist()
        return jsonify({'predictions': predictions})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=False)