import numpy as np


x = np.linspace(0, 10, 101)
print(x)

# Generate sine and cosine waves
sin_wave = np.sin(x)
cos_wave = np.cos(x)

# Save the sine and cosine waves to .npy files
np.save('/home/pi/ee347/lab-4-advanced-python-group-13/task7_sin.npy', sin_wave)
np.save('/home/pi/ee347/lab-4-advanced-python-group-13/task7_cos.npy', cos_wave)

print("Sine and cosine waves have been saved to 'task7_sin.npy' and 'task7_cos.npy' respectively.")