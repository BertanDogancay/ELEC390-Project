import pandas as pd
import matplotlib.pyplot as plt


walk_dataset = pd.read_csv('raw_data\jump\jump_combined_shuffled.csv')

time = walk_dataset.iloc[:,0]
accelerations = walk_dataset.iloc[:,1:5]

plt.plot(time, accelerations)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
  
# giving a title to my graph
plt.title('My first graph!')
  
# function to show the plot
plt.show()