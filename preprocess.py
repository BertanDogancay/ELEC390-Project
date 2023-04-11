import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

column_headers = ['Time (s)', 
                  'Linear Acceleration x (m/s^2)', 
                  'Linear Acceleration y (m/s^2)', 
                  'Linear Acceleration z (m/s^2)', 
                  'Absolute acceleration (m/s^2)']

walk_dataset = pd.read_csv('raw_data\jump\jump_combined.csv')
jump_dataset = pd.read_csv('raw_data\walk\walk_combined.csv')

walk_dataset.columns = column_headers
jump_dataset.columns = column_headers

walk_time = walk_dataset.iloc[:,0]
walk_accels = walk_dataset.iloc[:,1]

jump_time = jump_dataset.iloc[:,0]
jump_accels = jump_dataset.iloc[:,1:5]

start_window = 5
end_window = 100
increment = 5


# plotting
lw=1
fig, ax = plt.subplots()
legend = ['Noisy']
ax.plot(walk_time, walk_accels, linewidth=lw)

# applying SMA
smas = []

for window_size in range(start_window, end_window+1, increment):
    sma = walk_dataset.rolling(window_size).mean()
    smas.append(sma)
    #sma.to_csv('sma '+str(window_size)+'.csv')
    sma_time = sma.iloc[:,0]
    sma_accels = sma.iloc[:,1]

    ax.plot(sma_time, sma_accels, linewidth=lw)
    legend.append('SMA ' + str(window_size))

ax.legend(legend)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Acceleration')
plt.show()

