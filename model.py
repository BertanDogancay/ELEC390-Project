import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score


def feature_extract(df):
    df['max_x'] = df['Linear Acceleration x (m/s^2)'].rolling(window=window_size).max()
    df['max_y'] = df['Linear Acceleration y (m/s^2)'].rolling(window=window_size).max()
    df['max_z'] = df['Linear Acceleration z (m/s^2)'].rolling(window=window_size).max()
    df['max_abs'] = df['Absolute acceleration (m/s^2)'].rolling(window=window_size).max()

    df['min_x'] = df['Linear Acceleration x (m/s^2)'].rolling(window=window_size).min()
    df['min_y'] = df['Linear Acceleration y (m/s^2)'].rolling(window=window_size).min()
    df['min_z'] = df['Linear Acceleration z (m/s^2)'].rolling(window=window_size).min()
    df['min_abs'] = df['Absolute acceleration (m/s^2)'].rolling(window=window_size).min()

    df['mean_x'] = df['Linear Acceleration x (m/s^2)'].rolling(window=window_size).mean()
    df['mean_y'] = df['Linear Acceleration y (m/s^2)'].rolling(window=window_size).mean()
    df['mean_z'] = df['Linear Acceleration z (m/s^2)'].rolling(window=window_size).mean()
    df['mean_abs'] = df['Absolute acceleration (m/s^2)'].rolling(window=window_size).mean()

    df['variance_x'] = df['Linear Acceleration x (m/s^2)'].rolling(window=window_size).var()
    df['variance_y'] = df['Linear Acceleration y (m/s^2)'].rolling(window=window_size).var()
    df['variance_z'] = df['Linear Acceleration z (m/s^2)'].rolling(window=window_size).var()
    df['variance_abs'] = df['Absolute acceleration (m/s^2)'].rolling(window=window_size).var()

    df.dropna(inplace=True)

# Use an SMA on the training data

df_train = pd.read_csv('data\\train_data.csv')
df_test = pd.read_csv('data\\test_data.csv')
window_size = 5

sma = df_train.iloc[:,0:-1].rolling(window_size).mean()
sma['label'] = df_train.iloc[:,-1]
sma = sma.dropna()


# Do feature extraction on train and test data
window_size = 500

feature_extract(sma)
feature_extract(df_test)

# Normalize the data
# Separate input features from target variable
X_train = sma.drop('label', axis=1)
X_test = df_test.drop('label', axis=1)

# Normalize input features and store them
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

# Separate the target variable from the normalized input features
y_train = sma['label']
y_test = df_test['label']


# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model on the test set
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

recall = recall_score(y_test, y_pred) 
print('recall is: ', recall) 