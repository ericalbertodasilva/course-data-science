from scipy.stats import poisson

print("Average car accidents is 2 per day")

print("What is the likelihood of 3 accidents in the day?", poisson.pmf(3, 2))

print("What is the likelihood of 3 or fewer accidents in the day?", poisson.cdf(3, 2))

print("What is the likelihood of more than 3 accidents in the day?", poisson.sf(3, 2))
