import pickle
from model import feature_extract
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

def predict(filename):
    # load the model from the file
    model_name = 'logistic_regression_model.sav'
    loaded_model = pickle.load(open(model_name, 'rb'))

    # bring in a test file
    X_test = pd.read_csv(filename)

    # Do feature extraction on test data
    window_size = 50

    feature_extract(X_test)
    X_test = X_test.iloc[:,5:]

    # # normalize input features and store them
    scaler = StandardScaler()
    X_test = scaler.fit_transform(X_test)

    # use the model to make predictions
    y_pred = loaded_model.predict(X_test)

    # export predictions to csv file 'output.csv'
    df_y_pred = pd.DataFrame(data=y_pred, columns=['predicted label'])
    df_output = pd.read_csv(filename)
    df_output = pd.concat([df_output, df_y_pred], axis=1)
    df_output.to_csv('output.csv', index=False)

# put a csv as filename to predict labels and output csv
predict('jumptest.csv')

