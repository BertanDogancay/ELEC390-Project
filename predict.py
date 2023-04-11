import pickle
from model import feature_extract
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


# load the model from the file
filename = 'logistic_regression_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# bring in a test file
X_test = pd.read_csv('Raw Data.csv')

# extract it's features
feature_extract(X_test)

# # normalize input features and store them
# scaler = StandardScaler()
# X_test = scaler.fit_transform(X_test)

# use the model to make predictions
y_pred = loaded_model.predict_proba(X_test)
for pred in y_pred:
    print(pred)