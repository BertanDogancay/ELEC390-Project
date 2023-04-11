import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.decomposition import PCA



# reading the dataset and binarizing the labels 
train_set = pd.read_csv('data\\train.csv')
test_set = pd.read_csv('data\\test.csv')

train_data = train_set.iloc[:,2:10]
train_labels = train_set.iloc[:,10]

test_data = test_set.iloc[:,2:10]
test_labels = test_set.iloc[:,10]

print(train_data)
print(test_data)
print(train_labels)
print(test_labels)


# Define a Standard Scaler to normalize inputs 
scaler = StandardScaler() 
# # defining the classifier and the pipeline 
l_reg = LogisticRegression(max_iter=10000) 
clf = make_pipeline(StandardScaler(), l_reg) 
# training 
clf.fit(train_data, train_labels) 

# obtaining the predictions and the probabilities 
y_pred = clf.predict(test_data) 
y_clf_prob = clf.predict_proba(test_data) # y_clf_prob[:, 1] is the probability of the positive class for each sample 
print('y_pred is:', y_pred) 
print('y_clf_prob is:', y_clf_prob) 

# obtaining the classification accuracy 
acc = accuracy_score(test_labels, y_pred) 
print('accuracy is ', acc) 
# obtaining the classification recall 
recall = recall_score(test_labels, y_pred) 
print('recall is: ', recall) 
