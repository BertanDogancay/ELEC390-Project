import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

# extract datasets
walking_dataset = pd.read_csv("raw_data\conrad_walking.csv")
jumping_dataset = pd.read_csv("raw_data\conrad_jumping1.csv")

# separate walking data and get average
time = walking_dataset["Time (s)"]
x_walk_avg = np.mean(walking_dataset["Linear Acceleration x (m/s^2)"])
y_walk_avg = np.mean(walking_dataset["Linear Acceleration y (m/s^2)"])
z_walk_avg = np.mean(walking_dataset["Linear Acceleration z (m/s^2)"])
abs_walk_avg = np.mean(walking_dataset["Absolute acceleration (m/s^2)"])

# separate jumping data and get average
time = walking_dataset["Time (s)"]
x_jump_avg = np.mean(jumping_dataset["Linear Acceleration x (m/s^2)"])
y_jump_avg = np.mean(jumping_dataset["Linear Acceleration y (m/s^2)"])
z_jump_avg = np.mean(jumping_dataset["Linear Acceleration z (m/s^2)"])
abs_jump_avg = np.mean(jumping_dataset["Absolute acceleration (m/s^2)"])


X = ['X','Y','Z','Absolute']
avg_walk_accel = [x_walk_avg, y_walk_avg, z_walk_avg, abs_walk_avg]
avg_jump_accel = [x_jump_avg, x_jump_avg, z_jump_avg, abs_jump_avg]

X_axis = np.arange(len(X))

plt.bar(X_axis - 0.2, avg_walk_accel, 0.4, label = 'Walking')
plt.bar(X_axis + 0.2, avg_jump_accel, 0.4, label = 'Jumping')
  
plt.xticks(X_axis, X)
plt.xlabel("Acceleration Types")
plt.ylabel("Average Acceleration (m/s^2)")
plt.title("Average Accelerations of Jumping vs. Walking")
plt.legend()
plt.show()
