import pandas as pd
from sklearn.model_selection import train_test_split
import h5py
import numpy as np

##make sure to change the name of the raw data file
df = pd.read_csv('raw_data/<raw-data-name>.csv')

train_data, test_data = train_test_split(df, test_size=0.1, random_state=42, shuffle=False)
train_data.to_csv('data/train_data.csv', header=False, index=False)
test_data.to_csv('data/test_data.csv', header=False, index=False)

train_data = np.loadtxt('data/train_data.csv', delimiter=',')
test_data = np.loadtxt('data/test_data.csv', delimiter=',')

hdf5_file = h5py.File("data/data.hdf5", "w")
hdf5_file.close()

with h5py.File('data/data.hdf5', 'w') as f:
    group = f.create_group('Dataset')
    train_dataset = group.create_dataset('train', data=train_data, dtype=train_data.dtype)
    test_dataset = group.create_dataset('test', data=test_data, dtype=test_data.dtype)
    f.create_group('Bertan')
    f.create_group('Conrad')
    f.create_group('Ethan')

    print(f.keys())

with h5py.File('data/data.hdf5', 'r') as f:
    dataset = f['Dataset/test']
    column_data = dataset[:, 0]
    print(column_data)


