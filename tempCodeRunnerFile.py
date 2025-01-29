import numpy as np
from sklearn.linear_model import LinearRegression

# Function to predict the next number
def predict_next_number(last_data):
    # Extract features (time steps)
    X = np.arange(1, len(last_data) + 1).reshape(-1, 1)
    
    # Reshape last_data for compatibility with sklearn
    y = np.array(last_data).reshape(-1, 1)
    
    # Create and fit the model
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict the next value trend using linear regression
    next_time_step = len(last_data) + 1
    next_trend = model.predict([[next_time_step]])[0][0]
    
    # Add some randomness based on the trend
    next_trend += np.random.normal(0, 0.5)  # Adjust the standard deviation as needed
    
    # Ensure the predicted value is within the range [1, 10]
    next_prediction = min(10, max(1, next_trend))
    
    # Introduce a 2% chance of crash at value 1
    if next_prediction == 1 and np.random.rand() <= 0.02:
        next_prediction = np.random.randint(2, 11)  # Random value between 2 and 10
    
    return next_prediction

# Example dataset
last_data = [  
             3.34, 3.97, 1.86, 1.22, 1.47, 1.28, 1.22, 3.31, 2.26, 1.34,
             2.70, 1.18, 2.21, 2.87, 3.21, 1.23, 1.10, 9.32, 3.20, 1.39, 
             8.45, 1.69, 2.22, 3.34, 3.97, 1.86, 1.22, 1.47, 1.28, 1.22, 
             3.31,7.32,1.46,9.26,1.52,1.87,1.28,6.26,1.07,2.50,1.78,3.27,
             1.36,1.38,1.54,6.59,9.32,2.08,1.48,4.85,1.04,1.01,4.94,1.39,
             3.02,1.13,1.04,1.21,2.70,1.45,1.35,5.31,3.46,3.40,1.00,2.92,
             1.16,3.12,2.50,1.22,7.46,1.00,1.48,4.69,5.81,1.67,1.73,6.98,
             2.44,3.67,1.03,3.62,1.38,2.38,3.30,1.43,7.42,5.08,1.51,3.61
             ,3.10,4.33,2.09,1.12,3.66,1.32,2.38,5.57,3.03,1.44,7.99,1.64,8.59,7.63,3.51,3.16,1.63,1.50,1.51,1.12,2.22,1.75,8.96,2.07,1.77,1.73,1.00,5.91]

# Make prediction
next_prediction = predict_next_number(last_data)
print("Next predicted number:", next_prediction)
