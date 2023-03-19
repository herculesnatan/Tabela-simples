import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values,squares)

# Set chart title and label axes.

plt.title("Squares Numbers")
plt.xlabel("Value")
plt.ylabel("Square of Value")

# Set size of tick labels
plt.tick_params(axis='both')
plt.show()
