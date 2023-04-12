import pandas as pd
from sklearn.model_selection import train_test_split
import h5py
import numpy as np
import os



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
    os.chdir('..')
    os.chdir('..')


f = h5py.File('data\data.hdf5','w')
dataset = f.create_group("dataset")
conrad = f.create_group("conrad")
bertan = f.create_group("bertan")
ethan = f.create_group("ethan")

df = pd.read_csv('data\combined_data_shuffled.csv')

train_data, test_data = train_test_split(df, test_size=0.1, random_state=0, shuffle=False)

train_data.to_csv('data\\train_data.csv', index=False)
test_data.to_csv('data\\test_data.csv', index=False)

train_data = np.loadtxt('data\\train_data.csv', delimiter=',', skiprows=1)
test_data = np.loadtxt('data\\test_data.csv', delimiter=',', skiprows=1)
    
dataset.create_dataset('train', data=train_data)
dataset.create_dataset('test', data=test_data)

def create_dataset(type, file, group):
    df = pd.read_csv(file)          # 'raw_data\walk\walk_combined_shuffled.csv'

    train_filename = 'data/' + type + '_train_data.csv'
    test_filename = 'data/' + type + '_test_data.csv'

    train_data, test_data = train_test_split(df, test_size=0.1, random_state=0, shuffle=False)
    train_data.to_csv(train_filename, header=False, index=False)
    test_data.to_csv(test_filename, header=False, index=False)

    train_data = np.loadtxt(train_filename, delimiter=',')
    test_data = np.loadtxt(test_filename, delimiter=',')
    
    group.create_dataset(type+'_train', data=train_data)
    group.create_dataset(type+'_test', data=test_data)

# create_dataset('walk', 'data\walk_data_shuffled.csv', dataset)
# create_dataset('jump', 'data\jump_data_shuffled.csv', dataset)

store_member_data(conrad, 'conrad')
store_member_data(bertan, 'bertan')
# store_member_data(ethan, 'ethan')