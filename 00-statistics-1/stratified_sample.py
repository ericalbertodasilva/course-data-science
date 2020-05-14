import pandas as pd
from sklearn.model_selection import train_test_split

db_iris = pd.read_csv('iris.csv')
print(db_iris['class'].value_counts())

X_iris, _, y_iris, _ = train_test_split(db_iris.iloc[:, 0:4],
                              db_iris.iloc[:, 4],
                              test_size = 0.5,
                              stratify = db_iris.iloc[:,4])
print(y_iris.value_counts())

db_infert = pd.read_csv('infert.csv')
print(db_infert['education'].value_counts())

X_infert, _, y_infert, _ = train_test_split(db_infert.iloc[:, 2:9],
                                db_infert.iloc[:, 1],
                                test_size = 0.6,
                                stratify = db_infert.iloc[:, 1])
print(y_infert.value_counts())