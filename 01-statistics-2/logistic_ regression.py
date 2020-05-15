import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression

data_set_eleicao = pd.read_csv('Eleicao.csv', sep =';')
plt.scatter(data_set_eleicao.DESPESAS, data_set_eleicao.SITUACAO)
data_set_eleicao.describe()

np.corrcoef(data_set_eleicao.DESPESAS, data_set_eleicao.SITUACAO)

X = data_set_eleicao.iloc[:, 2].values
X = X[:, np.newaxis]
y = data_set_eleicao.iloc[:, 1].values

model_logistic_regression = LogisticRegression()
model_logistic_regression.fit(X, y)

print("interception of the trained model: ", model_logistic_regression.intercept_)
print("Inclination of trained model: ", model_logistic_regression.coef_)

plt.scatter(X, y)

X_test = np.linspace(10, 3000, 100)

def model(x):
    return 1 / (1 + np.exp(-x))

r = model(X_test * model_logistic_regression.coef_ + model_logistic_regression.intercept_).ravel()
plt.plot(X_test, r, color ='red')

date_set_predictions = pd.read_csv('NovosCandidatos.csv', sep =';')
expenses = date_set_predictions.iloc[:, 1].values
expenses = expenses.reshape(-1, 1)
predictions_test = model_logistic_regression.predict(expenses)
date_set_predictions = np.column_stack((date_set_predictions, predictions_test))