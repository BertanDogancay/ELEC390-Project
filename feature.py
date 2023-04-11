import pandas as pd
import os

def features(filename):
    dataset = pd.read_csv(filename)

    features = pd.DataFrame(columns=['max', 'min', 'mean', 'median', 'var', 'skew', 'std', 'kurt'])

    window_size = 500

    features['max'] = dataset.iloc[1:,4].rolling(window=window_size).max()
    features['min'] = dataset.iloc[1:,4].rolling(window=window_size).min()
    features['mean'] = dataset.iloc[1:,4].rolling(window=window_size).mean()
    features['median'] = dataset.iloc[1:,4].rolling(window=window_size).median()
    features['var'] = dataset.iloc[1:,4].rolling(window=window_size).var()
    features['skew'] = dataset.iloc[1:,4].rolling(window=window_size).skew()
    features['std'] = dataset.iloc[1:,4].rolling(window=window_size).std()
    features['kurt'] = dataset.iloc[1:,4].rolling(window=window_size).kurt()

    # add labels 0 for walking 1 for jumping
    if 'walk' in filename:
        features['label'] = 0
    elif 'jump' in filename:
        features['label'] = 1
    else:
        print("Couldn't identify type")

    features = features.dropna()
    print(filename)
    print(features)
    features.to_csv('features_'+filename[:-4]+'.csv')

os.chdir('data')
folder = os.listdir()
for file in folder:
    if '.csv' in file:
        features(file)

train_walk = pd.read_csv('features_walk_train_data.csv')
train_jump = pd.read_csv('features_jump_train_data.csv')
test_walk = pd.read_csv('features_walk_test_data.csv')
test_jump = pd.read_csv('features_jump_test_data.csv')

train = pd.concat([train_walk, train_jump], ignore_index=True)
test = pd.concat([test_walk, test_jump], ignore_index=True)

train.to_csv('train.csv')
test.to_csv('test.csv')