import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import ResidualsPlot

dataset_cars = pd.read_csv('cars.csv')
dataset_cars = dataset_cars.drop(['Unnamed: 0'], axis = 1)

X = dataset_cars.iloc[:, 1].values
y = dataset_cars.iloc[:, 0].values
correlation = np.corrcoef(X, y)

X = X.reshape(-1, 1)

model_linear_regression = LinearRegression()
model_linear_regression.fit(X, y)

print("interception of the trained model: ", model_linear_regression.intercept_)
print("Inclination of trained model: ", model_linear_regression.coef_)

plt.scatter(X, y)
plt.plot(X, model_linear_regression.predict(X), color = 'red')

distance_stop = np.array([[22]])

model_linear_regression.predict(distance_stop)

print("Residues of the trained model: ", model_linear_regression._residues)

visualization = ResidualsPlot(model_linear_regression)
visualization.fit(X, y)
visualization.poof()
