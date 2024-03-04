import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('web.html')

@app.route('/predict', methods = ['POST'])
def predict():
    float_features = [float(X) for X in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template('web.html', prediction_text = 'The Predicted close price of etherium is{}'.format(prediction))

if __name__ == "__main__":
    app.run(debug=True)