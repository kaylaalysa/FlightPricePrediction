import os # type: ignore
from flask import Flask, render_template, request # type: ignore
import pickle # type: ignore
import numpy as np # type: ignore
import joblib # type: ignore
from babel import numbers # type: ignore
import pandas as pd # type: ignore
import pickle # type: ignore
from sklearn.preprocessing import StandardScaler # type: ignore

app = Flask(__name__)
# app.secret_key = 'supersecretkey'

# Load model
model = joblib.load("best_model_rf.pkl")

# model = pickle.load(open('best_model_rf.pkl', 'rb'))
scaler_features = pickle.load(open('scaler_features.pkl', 'rb'))
scaler_target = pickle.load(open('scaler_target.pkl', 'rb'))

def format_currency(amount):
    return numbers.format_currency(amount, 'INR', locale='en_IN')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/formpredict')
def formpredict():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get data from form
        airline = float(request.form['airline'])
        flight = float(request.form['flight'])
        source_city = float(request.form['source_city'])
        departure_time = float(request.form['departure_time'])
        stops = float(request.form['stops'])
        arrival_time = float(request.form['arrival_time'])
        destination_city = float(request.form['destination_city'])
        travel_class = float(request.form['travel_class'])
        duration = float(request.form['duration'])
        days_left = float(request.form['days_left'])

        # Create feature array
        # features = np.array([[airline, flight,source_city, departure_time, stops, arrival_time, destination_city, travel_class, duration, days_left]])

        # X_scaled = scaler_features.transform(features)

        feature_names = ['airline', 'flight', 'source_city', 'departure_time', 'stops', 'arrival_time', 'destination_city', 'travel_class', 'duration', 'days_left']
        features_df = pd.DataFrame([[airline, flight, source_city, departure_time, stops, arrival_time, destination_city, travel_class, duration, days_left]],
                                columns=feature_names)

        X_scaled = scaler_features.transform(features_df)

        # Predict using the model
        y_pred = model.predict(X_scaled)
        y_pred_inversed = scaler_target.inverse_transform(y_pred.reshape(-1, 1))[0][0]

        return render_template('form.html', prediction=format_currency(round(y_pred_inversed, 2)))
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)