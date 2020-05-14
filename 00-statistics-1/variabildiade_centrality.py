import numpy as np
from scipy import stats

players = [40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000]
print("Mean: "+ str(np.mean(players)))
print("Median: "+ str(np.median(players)))

quartiles = np.quantile(players, [0, 0.25, 0.5, 0.75, 1])
print("Quartis: " + str(np.std(players, ddof = 1)))

print(str(stats.describe(players)))