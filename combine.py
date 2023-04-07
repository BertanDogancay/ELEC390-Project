import os
import pandas as pd




def combine_csv(folder):
    files = os.listdir()
    time_counter = 0
    times_to_add = []
    dataset_array = []

    for i in range(0, len(files)-1):
        # get last recorded time from dataset
        dataset = pd.read_csv(files[i])
        last_time = dataset["Time (s)"].iloc[-1]
        time_counter += last_time
        times_to_add.append(time_counter)

    dataset = pd.read_csv(files[0])
    dataset_array.append(dataset)

    for i in range(1, len(files)):
        dataset = pd.read_csv(files[i])
        dataset.iloc[:,0] += times_to_add[i-1]
        dataset_array.append(dataset)

    combined = pd.concat(dataset_array)

    combined.to_csv(folder+'_combined.csv', index=False)

os.chdir('raw_data')
folders = os.listdir()
for folder in folders:
    os.chdir(folder)
    combine_csv(folder)
    os.chdir('..')
