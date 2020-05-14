from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt

date = norm.rvs(size = 100)
stats.probplot(date, plot = plt)

print("Shapiro test " + str(stats.shapiro(date)))