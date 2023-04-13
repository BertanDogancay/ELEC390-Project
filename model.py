import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score
import pickle


def feature_extract(df, window_size=50):
    # Mean of acceleration
    df['mean_x'] = df['Linear Acceleration x (m/s^2)'].rolling(window=window_size).mean()
    df['mean_y'] = df['Linear Acceleration y (m/s^2)'].rolling(window=window_size).mean()
    df['mean_z'] = df['Linear Acceleration z (m/s^2)'].rolling(window=window_size).mean()
    df['mean_abs'] = df['Absolute acceleration (m/s^2)'].rolling(window=window_size).mean()
    # Standard deviation of acceleration
    df['std_x'] = df['Linear Acceleration x (m/s^2)'].rolling(window=window_size).std()
    df['std_y'] = df['Linear Acceleration y (m/s^2)'].rolling(window=window_size).std()
    df['std_z'] = df['Linear Acceleration z (m/s^2)'].rolling(window=window_size).std()
    df['std_abs'] = df['Absolute acceleration (m/s^2)'].rolling(window=window_size).std()
    # Skewness of acceleration components
    df['skew_x'] = df['Linear Acceleration x (m/s^2)'].rolling(window=window_size).skew()
    df['skew_y'] = df['Linear Acceleration y (m/s^2)'].rolling(window=window_size).skew()
    df['skew_z'] = df['Linear Acceleration z (m/s^2)'].rolling(window=window_size).skew()
    df['skew_abs'] = df['Absolute acceleration (m/s^2)'].rolling(window=window_size).skew()
    # Kurtosis of acceleration components
    df['kurt_x'] = df['Linear Acceleration x (m/s^2)'].rolling(window=window_size).kurt()
    df['kurt_y'] = df['Linear Acceleration y (m/s^2)'].rolling(window=window_size).kurt()
    df['kurt_z'] = df['Linear Acceleration z (m/s^2)'].rolling(window=window_size).kurt()
    df['kurt_abs'] = df['Absolute acceleration (m/s^2)'].rolling(window=window_size).kurt()
    # Correlations between acceleration components
    df['x_y_corr'] = df['Linear Acceleration x (m/s^2)'].rolling(window=window_size).corr(df['Linear Acceleration y (m/s^2)'])
    df['x_z_corr'] = df['Linear Acceleration x (m/s^2)'].rolling(window=window_size).corr(df['Linear Acceleration z (m/s^2)'])
    df['y_z_corr'] = df['Linear Acceleration y (m/s^2)'].rolling(window=window_size).corr(df['Linear Acceleration z (m/s^2)'])

    df.dropna(inplace=True)

def create_model():
    # Use an SMA on the training data
    df_train = pd.read_csv('data/train_data.csv')
    df_test = pd.read_csv('data/test_data.csv')
    window_size = 31

    sma = df_train.iloc[:,0:-1].rolling(window_size).mean()
    sma['label'] = df_train.iloc[:,-1]
    sma = sma.dropna()

    # Do feature extraction on train and test data
    window_size = 50

    feature_extract(sma)
    feature_extract(df_test)

    # get rid of raw data (time and accels)
    sma = sma.iloc[:,5:]
    df_test = df_test.iloc[:,5:]

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
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Evaluate the model on the test set
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    recall = recall_score(y_test, y_pred) 
    print('recall is: ', recall) 

    # save the model to a file
    filename = 'logistic_regression_model.sav'
    pickle.dump(model, open(filename, 'wb'))
