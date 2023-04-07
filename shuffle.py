import math
import pandas as pd
from sklearn.model_selection import train_test_split
import h5py
import numpy as np
import os
import random


shuffle_interval = 5



def shuffle_csv(filename, interval):
    segment_indexes = [0]
    segments = []
    
    # bring in dataset
    dataset = pd.read_csv(filename)
    time = dataset.iloc[:,0]

    # calculate how many 5 second intervals there are in the data
    num_segments = (time[len(time)-1] / interval).astype(int) + 1

    # search for indexes where 5 second windows start
    for i in range(1, num_segments):
        index = np.searchsorted(time, interval*i, side="left")
        segment_indexes.append(index)

    # divide into 5 second segments
    for index in range(0, len(segment_indexes)-1):
        start = segment_indexes[index]
        end = segment_indexes[index + 1]
        segments.append(dataset.iloc[start:end,:])

    # shuffle segments
    random.shuffle(segments)
    segments = pd.concat(segments)

    filename = filename[0:-4]

    segments.to_csv(filename+'_shuffled.csv', index=False)



os.chdir('raw_data')
folders = os.listdir()
for folder in folders:
    os.chdir(folder)
    files = os.listdir()
    for file in files:
        if 'combined' in file:
            print(file)
            shuffle_csv(file, shuffle_interval)
    os.chdir('..')





