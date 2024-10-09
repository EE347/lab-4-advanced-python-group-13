import numpy as np
import matplotlib.pyplot as plt


# Load the .npy file
file1 = np.load('/home/pi/ee347/lab-4-advanced-python-group-13/task7_sin.npy')
file2 = np.load('/home/pi/ee347/lab-4-advanced-python-group-13/task7_cos.npy')

# Plot the data
plt.plot(file1, label = 'sin(x)')
plt.plot(file2, label = 'cos(x)')
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Your Plot Title')

plt.legend()
plt.show()

