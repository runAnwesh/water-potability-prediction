import pandas as pd
import numpy as np
import os
import pickle
from sklearn.ensemble import RandomForestClassifier

train_data = pd.read_csv("./data/processed/train_processed.csv")

#X_train = train_data.iloc[:,0:-1].values
#Y_train = train_data.iloc[:,-1].values

X_train = train_data.drop(columns=['Potability'],axis=1)
Y_train = train_data['Potability']

clf = RandomForestClassifier()
clf.fit(X_train,Y_train)

pickle.dump(clf,open("model.pkl","wb"))

