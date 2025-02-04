from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('clv_model.pkl')


@app.route("/", methods=["GET"])
def home():
    return "Welcome!", 200
@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the POST request
    data = request.get_json()

    # Extract features (make sure they are in the same order as in training)
    recency = data['Recency']
    frequency = data['Frequency']
    age = data['Age']
    
    # Prepare input for model
    features = np.array([[recency, frequency, age]])
    
    # Make prediction
    prediction = model.predict(features)
    
    # Return the prediction as a JSON response
    return jsonify({'CLV': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True, port=5001) 
