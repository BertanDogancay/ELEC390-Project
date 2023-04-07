import pandas as pd
from sklearn.model_selection import train_test_split
import h5py
import numpy as np
import os

os.chdir('raw_data')

files = os.listdir()

dataset = pd.read_csv('conrad_walking.csv')

time = dataset.iloc[:,0]

print(time)