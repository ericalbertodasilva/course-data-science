import numpy as np
import pandas as pd
from math import ceil

population = 150
sample = 15
k = ceil(population / sample)

r = np.random.randint(low = 1,
                      high = k + 1,
                      size = 1)

accumulate = r[0]
raffle = []
for i in range(sample):
    raffle.append(accumulate)
    accumulate += k
    
base_iris = pd.read_csv('iris.csv')
print(len(base_iris))
base_iris_final = base_iris.loc[raffle]
print(len(base_iris_final))