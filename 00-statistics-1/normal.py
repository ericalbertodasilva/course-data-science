from scipy.stats import norm

print("Set of objects in a basket, the average is 8 and the standard deviation is 2," +
      " What is the probability of taking an object that weight is less than 6 kilos?" + str(norm.cdf(6, 8, 2)))

print("What is the probability of removing an object that weighs more than 6 kilos?" + str(1 - norm.cdf(6, 8, 2)))

print("What is the probability of taking an object that the weight is less than " +
      "6 or greater than 10 kg?" + str(norm.cdf(6, 8, 2) + norm.sf(10, 8, 2)))

print("What is the probability of taking an object that the weight is less than " +
      "10 and greater than 8 kilos?" + str(norm.cdf(10, 8, 2) - norm.cdf(8, 8, 2)))
