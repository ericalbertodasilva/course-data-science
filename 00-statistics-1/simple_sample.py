import pandas as pd
import numpy as np

base = pd.read_csv('iris.csv')
print(base)

print(base.shape)

np.random.seed(2345)
sample = np.random.choice(a = [0, 1],
                          size = 150,
                          replace = True,
                          p = [0.5, 0.5])

print(len(sample))
print(len(sample[sample == 1]))
print(len(sample[sample == 0]))
