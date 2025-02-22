import pandas as pd
import numpy as np
import os
import pickle
import yaml
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
"""
Hyperparameter tuning using GridSearchCV

param_grid = {'max_features': ['sqrt', 'log'], 'criterion': ['gini', 'entropy', 'log_loss']}


"""

def load_params(params_path: str) -> int:
    try:
        with open(params_path,"r") as file:
            params = yaml.safe_load(file)
        return params["model_building"]["n_estimators"]
    except Exception as e:
        raise Exception(f"Error loading parameters from {params_path}: {e}")
    
def load_data(filepath : str) -> pd.DataFrame:
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        raise Exception(f"Error loading data from {filepath}:{e}")
    
#train_data = pd.read_csv("./data/processed/train_processed.csv")

#n_estimators = yaml.safe_load(open("params.yaml"))["model_building"]["n_estimators"]

def prepare_data(data: pd.DataFrame) -> tuple[pd.DataFrame,pd.Series]:
    try:
        X = data.drop(columns=['Potability'],axis=1)
        Y = data['Potability']
        return X, Y
    except Exception as e:
        raise Exception(f"Error preparing data: {e}")

def train_model(X: pd.DataFrame, Y: pd.Series, n_estimators: int) -> RandomForestClassifier:
    try:
        clf = RandomForestClassifier(n_estimators=n_estimators)
        clf.fit(X,Y)
        return clf
    except Exception as e:
        raise Exception(f"Error training model: {e}")

def save_model(model: RandomForestClassifier, filepath: str) -> None:
    try:
        with open(filepath,"wb") as file:
            pickle.dump(model,file)
    except Exception as e:
        raise Exception(f"Error saving model to {filepath}: {e}")

def main():
    try:
        params_path = "params.yaml"
        data_path = "./data/processed/train_processed.csv"
        model_name = "models/model.pkl"

        n_estimators = load_params(params_path)
        train_data = load_data(data_path)
        X_train, Y_train = prepare_data(train_data)

        model = train_model(X_train, Y_train, n_estimators)
        save_model(model, model_name)
        print("Model Trained and Saved Successfully!")
    except Exception as e:
        raise Exception(f"An error ocurred: {e}")
    

if __name__ == "__main__":
    main()