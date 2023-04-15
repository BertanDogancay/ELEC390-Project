import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import h5py

#GENERATE GRAPHS OF XYZ ACCELERATION FOR 3 RANDOM SETS OF JUMPING DATA
#window size for 5 seconds of data
window_size = 500

labels = ["Time", "X-axis Acceleration", "Y-axis Acceleration", "Z-axis Acceleration"]

#create dataframe from csv
dataset = pd.read_csv('data\\jump_data.csv')
dataset = pd.DataFrame(dataset)

fig, ax = plt.subplots(ncols=1, nrows=3, figsize=(10, 10))

for i in range (0,3):
    window_start = 1000*i
    window_end = window_start + window_size

    for j in range(0,3):
        ax.flatten()[j].plot(dataset.iloc[window_start:window_end,0],
        dataset.iloc[window_start:window_end,j+1])
        ax.flatten()[j].plot(dataset.iloc[window_start:window_end, 0],
        dataset.iloc[(window_start+1000):(window_end+1000), j + 1])
        ax.flatten()[j].plot(dataset.iloc[window_start:window_end, 0],
        dataset.iloc[(window_start+500):(window_end+500), j + 1])
        ax.flatten()[j].set_xlabel(labels[0])
        ax.flatten()[j].set_ylabel(labels[j+1])

    fig.suptitle("Acceleration vs Time - Jumping")
    plt.show()

##########################################################################
#GENERATE GRAPHS OF XYZ ACCELERATION FOR 3 RANDOM SETS OF WALKING DATA
dataset = pd.read_csv('data\\walk_data.csv')
dataset = pd.DataFrame(dataset)

fig, ax = plt.subplots(ncols=1, nrows=3, figsize=(10, 10))

for i in range (0,3):
    window_start = 1000*i
    window_end = window_start + window_size

    for j in range(0,3):
        ax.flatten()[j].plot(dataset.iloc[window_start:window_end,0],
        dataset.iloc[window_start:window_end,j+1])
        ax.flatten()[j].plot(dataset.iloc[window_start:window_end, 0],
        dataset.iloc[(window_start+1000):(window_end+1000), j + 1])
        ax.flatten()[j].plot(dataset.iloc[window_start:window_end, 0],
        dataset.iloc[(window_start+500):(window_end+500), j + 1])
        ax.flatten()[j].set_xlabel(labels[0])
        ax.flatten()[j].set_ylabel(labels[j+1])

    fig.suptitle("Acceleration vs Time - Walking")
    plt.show()

########################################################################
#GENERATE GRAPH FOR AVERAGE JUMPING ACCELERATION FOR EACH GROUP MEMBER
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

colors = ['r', 'g', 'b']
yticks = [2, 1, 0]

dataset = pd.read_csv('raw_data\jump\conrad_jumping_front_pocket.csv')
dataset = pd.DataFrame(dataset)

ax.bar(dataset.iloc[:, 0], dataset.iloc[:, 4], zs=2, zdir='y', color = 'r', alpha=0.8, width = 0.1)

dataset = pd.read_csv('raw_data\jump\ethan_jumping_front_pocket.csv')
dataset = pd.DataFrame(dataset)

ax.bar(dataset.iloc[:, 0], dataset.iloc[:, 4], zs=1, zdir='y', color = 'g', alpha=0.8, width = 0.1)

dataset = pd.read_csv('raw_data\jump\\bertan_jumping_front_pocket.csv')
dataset = pd.DataFrame(dataset)

ax.bar(dataset.iloc[:, 0], dataset.iloc[:, 4], zs=0, zdir='y', color = 'b', alpha=0.8, width = 0.1)

ax.set_xlabel('Time (s)')
ax.set_ylabel('Team Members')
ax.set_zlabel('Average Acceleration (m/s^2)')

# On the y-axis let's only label the discrete values that we have data for.
ax.set_yticks(yticks)

fig.suptitle("Trial Average Acceleration by Team Member")

plt.show()

##############################################################################
#GENERATE GRAPH FOR AVERAGE WALKING ACCELERATION FOR EACH GROUP MEMBER
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

colors = ['r', 'g', 'b']
yticks = [2, 1, 0]

dataset = pd.read_csv('raw_data\walk\conrad_walking_front_pocket.csv')
dataset = pd.DataFrame(dataset)

ax.bar(dataset.iloc[:, 0], dataset.iloc[:, 4], zs=2, zdir='y', color = 'r', alpha=0.8, width = 0.1)

dataset = pd.read_csv('raw_data\walk\ethan_walking_front_pocket.csv')
dataset = pd.DataFrame(dataset)

ax.bar(dataset.iloc[:, 0], dataset.iloc[:, 4], zs=1, zdir='y', color = 'g', alpha=0.8, width = 0.1)

dataset = pd.read_csv('raw_data\walk\\bertan_walking_front_pocket.csv')
dataset = pd.DataFrame(dataset)

ax.bar(dataset.iloc[:, 0], dataset.iloc[:, 4], zs=0, zdir='y', color = 'b', alpha=0.8, width = 0.1)

ax.set_xlabel('Time (s)')
ax.set_ylabel('Team Members')
ax.set_zlabel('Average Acceleration (m/s^2)')

# On the y-axis let's only label the discrete values that we have data for.
ax.set_yticks(yticks)

fig.suptitle("Trial Average Acceleration by Team Member")

plt.show()

##############################################################################

#GENERATE SCATTER PLOT OF ACCELERATION DATA IN DIFFERENT PHONE CONFIGURATIONS - JUMPING
fig = plt.figure()
ax = fig.add_subplot(projection = '3d')

dataset = pd.read_csv('raw_data\jump\ethan_jumping_arm_down.csv')
dataset = pd.DataFrame(dataset)

arm_down = ax.scatter(dataset.iloc[:,1],dataset.iloc[:,2],dataset.iloc[:,3], color = 'c', s=1)

dataset = pd.read_csv('raw_data\jump\ethan_jumping_arm_up.csv')
dataset = pd.DataFrame(dataset)

arm_up = ax.scatter(dataset.iloc[:,1],dataset.iloc[:,2],dataset.iloc[:,3], color = 'r', s=1)

dataset = pd.read_csv('raw_data\jump\ethan_jumping_back_pocket.csv')
dataset = pd.DataFrame(dataset)

front_pocket = ax.scatter(dataset.iloc[:,1],dataset.iloc[:,2],dataset.iloc[:,3], color = 'g', s=1)

dataset = pd.read_csv('raw_data\jump\ethan_jumping_front_pocket.csv')
dataset = pd.DataFrame(dataset)

back_pocket = ax.scatter(dataset.iloc[:,1],dataset.iloc[:,2],dataset.iloc[:,3], color = 'b', s=1)

dataset = pd.read_csv('raw_data\jump\ethan_jumping_coat_pocket.csv')
dataset = pd.DataFrame(dataset)

coat_pocket = ax.scatter(dataset.iloc[:,1],dataset.iloc[:,2],dataset.iloc[:,3], color = 'y', s=1)

ax.legend((arm_down, arm_up, front_pocket,back_pocket,coat_pocket), ('Arm Down', 'Arm Up', 'Front Pocket', 'Back Pocket', 'Coat Pocket'))

ax.set_xlabel('X-axis Acceleration (m/s^2)')
ax.set_ylabel('Y-axis Acceleration (m/s^2)')
ax.set_zlabel('Z-axis Acceleration (m/s^2)')

fig.suptitle("Acceleration by Phone Position - Jumping")

plt.show()

##############################################################################
#GENERATE SCATTER PLOT OF ACCELERATION DATA IN DIFFERENT PHONE CONFIGURATIONS - WALKING
fig = plt.figure()
ax = fig.add_subplot(projection = '3d')

dataset = pd.read_csv('raw_data\walk\ethan_walking_arm_down.csv')
dataset = pd.DataFrame(dataset)

arm_down = ax.scatter(dataset.iloc[:,1],dataset.iloc[:,2],dataset.iloc[:,3], color = 'c', s=1)

dataset = pd.read_csv('raw_data\walk\ethan_walking_arm_up.csv')
dataset = pd.DataFrame(dataset)

arm_up = ax.scatter(dataset.iloc[:,1],dataset.iloc[:,2],dataset.iloc[:,3], color = 'r', s=1)

dataset = pd.read_csv('raw_data\walk\ethan_walking_back_pocket.csv')
dataset = pd.DataFrame(dataset)

front_pocket = ax.scatter(dataset.iloc[:,1],dataset.iloc[:,2],dataset.iloc[:,3], color = 'g', s=1)

dataset = pd.read_csv('raw_data\walk\ethan_walking_front_pocket.csv')
dataset = pd.DataFrame(dataset)

back_pocket = ax.scatter(dataset.iloc[:,1],dataset.iloc[:,2],dataset.iloc[:,3], color = 'b', s=1)

dataset = pd.read_csv('raw_data\walk\ethan_walking_coat_pocket.csv')
dataset = pd.DataFrame(dataset)

coat_pocket = ax.scatter(dataset.iloc[:,1],dataset.iloc[:,2],dataset.iloc[:,3], color = 'y', s=1)

ax.legend((arm_down, arm_up, front_pocket,back_pocket,coat_pocket), ('Arm Down', 'Arm Up', 'Front Pocket', 'Back Pocket', 'Coat Pocket'))

ax.set_xlabel('X-axis Acceleration (m/s^2)')
ax.set_ylabel('Y-axis Acceleration (m/s^2)')
ax.set_zlabel('Z-axis Acceleration (m/s^2)')

fig.suptitle("Acceleration by Phone Position - Walking")

plt.show()
