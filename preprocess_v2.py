import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Use an SMA on the training data

df_train = pd.read_csv('data\\train_data.csv')
df_test = pd.read_csv('data\\test_data.csv')
window_size = 5

sma = df_train.iloc[:,0:-1].rolling(window_size).mean()
sma['label'] = df_train.iloc[:,-1]
sma = sma.dropna()

print(sma)

# Normalize the data
# Separate input features from target variable
X_train = sma.drop('label', axis=1)
X_test = df_test.drop('label', axis=1)

# Normalize input features
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