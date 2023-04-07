import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

walk_dataset = pd.read_csv('raw_data\conrad_jumping1.csv')

time = walk_dataset.iloc[:,0]
abs_accel = walk_dataset.iloc[:,4]


# applying SMA
window_size = 5
sma5 = abs_accel.rolling(window_size).mean()

window_size = 8
sma61 = abs_accel.rolling(window_size).mean()

# plotting
lw=1
fig, ax = plt.subplots(figsize=(10, 10))
ax.plot(time, abs_accel, linewidth=lw)
ax.plot(time, sma5, linewidth=lw)
ax.plot(time, sma61, linewidth=lw)

ax.legend(['noisy', 'SMA 5', 'SMA 8'])
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()