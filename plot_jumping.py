import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

dataset = pd.read_csv("raw_data\conrad_jumping1.csv")

# separate data
time = dataset["Time (s)"]
x_accel = dataset["Linear Acceleration x (m/s^2)"]
y_accel = dataset["Linear Acceleration y (m/s^2)"]
z_accel = dataset["Linear Acceleration z (m/s^2)"]
abs_accel = dataset["Absolute acceleration (m/s^2)"]

# create figure
fig = plt.figure(layout='constrained')

# create 2 x 2 grid space
gs = gridspec.GridSpec(2, 2, figure=fig, left=0.1)

# add axes to figure
axes_x = fig.add_subplot(gs[0,0])
axes_y = fig.add_subplot(gs[0,1])
axes_z = fig.add_subplot(gs[1,0])
axes_abs = fig.add_subplot(gs[1,1])

# plot axes
axes_x.plot(time, x_accel, 'r')
axes_y.plot(time, y_accel, 'g')
axes_z.plot(time, z_accel, 'b')
axes_abs.plot(time, abs_accel, 'm')

# axes set titles
axes_x.set_title('X Acceleration')
axes_y.set_title('Y Acceleration')
axes_z.set_title('Z Acceleration')
axes_abs.set_title('Absolute Acceleration')

# axes set labels
axes_x.set_xlabel('Time (s)')
axes_x.set_ylabel('X Acceleration (m/s^2)')

axes_y.set_xlabel('Time (s)')
axes_y.set_ylabel('Y Acceleration (m/s^2)')

axes_z.set_xlabel('Time (s)')
axes_z.set_ylabel('Z Acceleration (m/s^2)')

axes_abs.set_xlabel('Time (s)')
axes_abs.set_ylabel('Absolute Acceleration (m/s^2)')


fig.suptitle('Accelerations for Jumping')
plt.show()