# ✈️ Flight Price Prediction

Welcome to my Machine Learning portfolio project where I build a model to predict flight prices using real-world data!  

## 📊 Dataset

This project uses the [Flight Price Prediction Dataset](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction/data) from Kaggle.  
The dataset contains information like airline, source, destination, duration, total stops, and more.

Dataset contains information about flight booking options from the website Easemytrip for flight travel between India's top 6 metro cities. There are 300261 datapoints and 11 features in the cleaned dataset.

## Features
The various features of the cleaned dataset are explained below:
1) Airline: The name of the airline company is stored in the airline column. It is a categorical feature having 6 different airlines.
2) Flight: Flight stores information regarding the plane's flight code. It is a categorical feature.
3) Source City: City from which the flight takes off. It is a categorical feature having 6 unique cities.
4) Departure Time: This is a derived categorical feature obtained created by grouping time periods into bins. It stores information about the departure time and have 6 unique time labels.
5) Stops: A categorical feature with 3 distinct values that stores the number of stops between the source and destination cities.
6) Arrival Time: This is a derived categorical feature created by grouping time intervals into bins. It has six distinct time labels and keeps information about the arrival time.
7) Destination City: City where the flight will land. It is a categorical feature having 6 unique cities.
8) Class: A categorical feature that contains information on seat class; it has two distinct values: Business and Economy.
9) Duration: A continuous feature that displays the overall amount of time it takes to travel between cities in hours.
10)Days Left: This is a derived characteristic that is calculated by subtracting the trip date by the booking date.
11) Price: Target variable stores information of the ticket price.

## 🧠 Machine Learning Model

For this regression task, I implemented the **Random Forest Regressor**, a powerful ensemble learning method that works great for tabular data.

To get the best performance, I fine-tuned the hyperparameters using **RandomizedSearchCV**.

## 📈 Model Performance

Here are the performance metrics of the final tuned model:

| Metric            | Training Set | Validation Set |
|------------------|--------------|----------------|
| RMSE             | 0.0672       | 0.1097         |
| MSE              | 0.0045       | 0.0120         |
| MAE              | 0.0280       | 0.0468         |

🚀 The model shows good generalization ability, with relatively low errors on both training and validation sets.


## 🌐 Model Deployment

To make the model accessible to users, I deployed it through a simple web application using **Flask**.

### ⚙️ Deployment Features:
- A clean and intuitive web interface
- Users can input flight details like airline, source, destination, etc.
- Instantly get the predicted flight price after submitting the form

### 🛠 Tech Stack for Deployment:
- **Flask** for building the web server
- **HTML/CSS** for the frontend
- **Pickle** for model serialization

## 🧰 Tools & Libraries

- Python 
- Pandas & NumPy for data handling
- Scikit-learn for preprocessing, modeling, and evaluation
- Matplotlib & Seaborn for data visualization
- Flask for web deployment



## 🖼️ Web App Screenshots

### 🏠 Homepage
![Homepage Screenshot](https://github.com/user-attachments/assets/28dce2b4-3c48-40b6-9897-85d11544a60d)

### 🧾 Prediction Form
![Prediction Form Screenshot](https://github.com/user-attachments/assets/f5552ea5-0ae0-47fc-a418-91ed59c60620)

### 🙋‍♀️ About Me
![About Me Screenshot](https://github.com/user-attachments/assets/3e0bb1de-ea56-4ac4-bf51-24f4634334b8)
