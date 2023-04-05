import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

walking_dataset = pd.read_csv("raw_data\conrad_walking.csv")
jumping_dataset = pd.read_csv("raw_data\conrad_jumping1.csv")

# separate walking data
time_walk = walking_dataset["Time (s)"]
x_walk = walking_dataset["Linear Acceleration x (m/s^2)"]
y_walk = walking_dataset["Linear Acceleration y (m/s^2)"]
z_walk = walking_dataset["Linear Acceleration z (m/s^2)"]
abs_walk = walking_dataset["Absolute acceleration (m/s^2)"]

# separate jumping data
time_jump = jumping_dataset["Time (s)"]
x_jump = jumping_dataset["Linear Acceleration x (m/s^2)"]
y_jump = jumping_dataset["Linear Acceleration y (m/s^2)"]
z_jump = jumping_dataset["Linear Acceleration z (m/s^2)"]
abs_jump = jumping_dataset["Absolute acceleration (m/s^2)"]

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
lw=0.1

axes_x.plot(time_jump, x_jump, 'b', label='Jumping', linewidth=lw)
axes_x.plot(time_walk, x_walk, 'r', label='Walking', linewidth=lw)
axes_x.legend()

axes_y.plot(time_jump, y_jump, 'b', label='Jumping', linewidth=lw)
axes_y.plot(time_walk, y_walk, 'r', label='Walking', linewidth=lw)
axes_y.legend()

axes_z.plot(time_jump, z_jump, 'b', label='Jumping', linewidth=lw)
axes_z.plot(time_walk, z_walk, 'r', label='Walking', linewidth=lw)
axes_z.legend()

axes_abs.plot(time_jump, abs_jump, 'b', label='Jumping', linewidth=lw)
axes_abs.plot(time_walk, abs_walk, 'r', label='Walking', linewidth=lw)
axes_abs.legend()


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


fig.suptitle('Accelerations for Walking')
plt.show()