import pandas as pd
from sklearn.model_selection import train_test_split
import h5py
import numpy as np
import os

def create_dataset(type, file, group):
    df = pd.read_csv(file)          # 'raw_data\walk\walk_combined_shuffled.csv'

    train_filename = 'data/' + type + '_train_data.csv'
    test_filename = 'data/' + type + '_test_data.csv'

    train_data, test_data = train_test_split(df, test_size=0.1, random_state=42, shuffle=False)
    train_data.to_csv(train_filename, header=False, index=False)
    test_data.to_csv(test_filename, header=False, index=False)

    train_data = np.loadtxt(train_filename, delimiter=',')
    test_data = np.loadtxt(test_filename, delimiter=',')
    
    group.create_dataset(type+'_train', data=train_data)
    group.create_dataset(type+'_test', data=test_data)

def store_member_data(group, name):
    os.chdir('raw_data\jump')
    files = os.listdir()
    for file in files:
        if name in file:
            parsed_file = np.loadtxt(file, delimiter=',', skiprows=1)
            group.create_dataset(file[:-4], data=parsed_file)
    os.chdir('..')
    os.chdir('walk')
    files = os.listdir()
    for file in files:
        if name in file:
            parsed_file = np.loadtxt(file, delimiter=',', skiprows=1)
            group.create_dataset(file[:-4], data=parsed_file)


f = h5py.File('data\data.hdf5','w')
dataset = f.create_group("dataset")
conrad = f.create_group("conrad")
bertan = f.create_group("bertan")
ethan = f.create_group("ethan")

create_dataset('walk', 'raw_data\walk\walk_combined_shuffled.csv', dataset)
create_dataset('jump', 'raw_data\jump\jump_combined_shuffled.csv', dataset)

store_member_data(conrad, 'conrad')
# store_member_data(bertan, 'bertan')
# store_member_data(ethan, 'ethan')