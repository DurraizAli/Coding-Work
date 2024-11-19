import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.preprocessing import StandardScaler
print(os.getcwd())

# Sample data (x: input, y: output)
#df = pd.read_csv('data.csv')
df= pd.read_excel('Boston.xlsx')
print(df.isnull().sum())
X= df.iloc[:,:-1].values
y=df.iloc[:, -1].values # derivative wrt c

assert not np.isnan(X).any(), "Input contains NaN"
assert not np.isinf(X).any(), "Input contains infinite values"
assert not np.isnan(y).any(), "Output contains NaN"
assert not np.isinf(y).any(), "Output contains infinite values"

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X) 
y_mean = np.mean(y)
y_std = np.std(y)
y_scaled = (y - y_mean) / y_std

# Check if scaled values are within a reasonable range
assert np.all(np.abs(X_scaled) < 10), "Scaled values are too large"
# Initialize parameters
m = np.zeros(X.shape[1]) # slope
c = 0  # intercept
L = 0.0005  # learning rate
epochs = 3000  # number of iterations


# Gradient Descent Algorithm
for i in range(epochs):
    y_pred = np.dot(X,m) + c  # predicted y
    D_m = (-2 / len(X)) * np.dot(X_scaled.T , (y_scaled - y_pred))  # derivative wrt m
    D_c = (-2 / len(X)) * sum(y_scaled - y_pred)  #
    c = c - L * D_c  # update 
    m = m - L * D_m

print(f"Optimized parameters: m = {m}, c = {c}")

x_new = np.array([0.7089,7.99,0.665,8.55,44.7,2.4,4.09,3,322,21,350.8])

# Scale the new data point
# x_new_scaled = scaler.transform([x_new])

# Predict using the scaled new data point
x_new_scaled = scaler.transform([x_new])
y_pred_new = np.dot(x_new_scaled, m) + c
y_pred_new_original = y_pred_new * y_std + y_mean
print(f"The predicted value for the new data point is {y_pred_new_original}")

# print(df.columns)
# df.to_numpy()
# print(df)
