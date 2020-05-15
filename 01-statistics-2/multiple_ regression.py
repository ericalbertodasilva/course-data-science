import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sm

data_set_mt_cars = pd.read_csv('mt_cars.csv')
data_set_mt_cars = data_set_mt_cars.drop(['Unnamed: 0'], axis=1)

X = data_set_mt_cars.iloc[:, 2].values
y = data_set_mt_cars.iloc[:, 0].values
correlation = np.corrcoef(X, y)

X = X.reshape(-1, 1)

model_linear_regression = LinearRegression()
model_linear_regression.fit(X, y)

print("interception of the trained model: ", model_linear_regression.intercept_)
print("Inclination of trained model: ", model_linear_regression.coef_)
print("Score of trained model: ", model_linear_regression.score(X, y))


predictions = model_linear_regression.predict(X)
model_linear_regression_adjusted = sm.ols(formula='mpg ~ disp', data=data_set_mt_cars)
model_linear_regression_adjusted_fit = model_linear_regression_adjusted.fit()
model_linear_regression_adjusted_fit.summary()

plt.scatter(X, y)
plt.plot(X, predictions, color='red')

disp = np.array([[200]])

model_linear_regression.predict(disp)

X1 = data_set_mt_cars.iloc[:, 1:4].values
y1 = data_set_mt_cars.iloc[:, 0].values
model_linear_regression_2 = LinearRegression()
model_linear_regression_2.fit(X1, y1)

model_linear_regression_2.score(X1, y1)
model_linear_regression_adjusted_2 = sm.ols(formula='mpg ~ cyl + disp + hp', data=data_set_mt_cars)
model_linear_regression_adjusted_fit_2 = model_linear_regression_adjusted_2.fit()
model_linear_regression_adjusted_fit_2.summary()

cyl_disp_hp = np.array([4, 200, 100])
cyl_disp_hp = cyl_disp_hp.reshape(1, -1)
model_linear_regression_2.predict(cyl_disp_hp)

