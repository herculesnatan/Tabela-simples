import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c= (0,0,0),
            edgecolors='none' ,s=40)

# Set chart title and label axes
plt.title("Squares Numbers")
plt.xlabel("Value")
plt.ylabel("Square of Value")

# Set the range for each axis.
plt.axis([0,1100,0,1100000])
# Set size of tick labels
plt.tick_params(axis='both', which = 'major')
plt.show()