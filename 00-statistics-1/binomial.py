from scipy.stats import binom

probability = binom.pmf(3, 5, 0.5)
print("Throwing a coin 5 times, what is the probability of winning 3 times?"+str(probability))

print(" Go through 4 signs of 4 times, what is the probability of getting the green light" +
      " none, 1, 2, 3 or 4 times in a row?")
print("0: " + str(binom.pmf(0, 4, 0.25)))
print("1: " + str(binom.pmf(1, 4, 0.25)))
print("2: " + str(binom.pmf(2, 4, 0.25)))
print("3: " + str(binom.pmf(3, 4, 0.25)))
print("4: " + str(binom.pmf(4, 4, 0.25)))

probability = binom.pmf(4, 4, 0.5)
print("What if they are two-stroke signs? " + str(probability))

probability = binom.cdf(4, 4, 0.25)
print("Cumulative probability " + str(probability))

probability = binom.pmf(7, 12, 0.25) * 100
print("Contest with 12 questions, what is the probability of getting 7 questions right considering " +
      "that each question has 4 alternatives? \n" + str(probability))

probability = binom.pmf(12, 12, 0.25) * 100

print("Contest with 12 questions, what is the probability of getting 12 questions right considering " +
      "that each question has 4 alternatives? \n" + str(probability))