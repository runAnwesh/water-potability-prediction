import pandas as pd
import numpy as np
import os
import pickle
import yaml
from sklearn.ensemble import RandomForestClassifier

train_data = pd.read_csv("./data/processed/train_processed.csv")

n_estimators = yaml.safe_load(open("params.yaml"))["model_building"]["n_estimators"]

X_train = train_data.drop(columns=['Potability'],axis=1)
Y_train = train_data['Potability']

clf = RandomForestClassifier(n_estimators=n_estimators)
clf.fit(X_train,Y_train)

pickle.dump(clf,open("model.pkl","wb"))

