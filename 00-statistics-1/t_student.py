from scipy.stats import t

# Average salary of data scientists = R $ 75.00 per hour
# Sample with 9 employees and standard deviation = 10

print("How likely is it to select a data scientist and the salary is less than R $ 80 per hour? ", t.cdf(1.5, 8))

print("How likely is the salary to be greater than 80? ", (t.sf(1.5, 8) * 100), " %")