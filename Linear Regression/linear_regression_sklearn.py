import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

# Load dataset
df = pd.read_excel('Boston.xlsx')
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the data
# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

x_new = np.array([0.84054	,8.14	,0.538,	5.599,	85.7	,4.4546,	4	,307	,21, 303.42	,16.51]).reshape(1,-1)


# Predict and evaluate
y_pred = model.predict(x_new)
# mse = mean_squared_error(y_test, y_pred)

# print(f"Mean Squared Error: {mse}")
print(f"Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")

# # New data point
# x_new = np.array([0.7089,7.99,0.665,8.55,44.7,2.4,4.09,3,322,21,350.8])
# x_new_scaled = scaler.transform([x_new])
# y_pred_new = model.predict(x_new_scaled.reshape(1, -1))

print(f"The predicted value for the new data point is {y_pred}")