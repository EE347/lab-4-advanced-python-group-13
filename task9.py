import csv
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data
data = pd.read_csv('/home/pi/ee347/lab-4-advanced-python-group-13/task9.csv')

# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')

# Set the 'Date' column as the index
data.set_index('Date', inplace=True)

# Plot the data
plt.figure(figsize=(10, 6))
for column in data.columns:
    plt.plot(data.index, data[column], label=column)

plt.xlabel('Date')
plt.ylabel('Stock Prices')
plt.title('Stock Prices Over Time')
plt.legend()
plt.grid(True)
plt.show()
