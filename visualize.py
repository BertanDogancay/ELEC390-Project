import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv("raw_data\conrad_walking.csv")

labels = list(dataset.columns)
time = dataset.iloc[:,0]
x = dataset.iloc[:,1]
print(x)

fig, ax = plt.subplots()

ax.plot(time, x, linewidth=2.0)


plt.show()

#data = dataset.iloc[]