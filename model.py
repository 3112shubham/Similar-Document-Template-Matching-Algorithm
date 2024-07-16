import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from utils.maps import gen,loc,med,pol,dia,pla,spe
from sklearn.datasets import load_iris
def value(x):
    return x.split(",")

def mod(dat):
    data = pd.read_csv('./insurance_data.csv')

    x = data[["PolicyHolder ID","Age","Gender","Location","Medical History","Policy Type","Procedure Code","Diagnosis Codes","Treatment Cost","Place Of Service","Provider ID","Specialization"]]
    y = data["Fraudulent"]

    model = RandomForestClassifier(n_estimators=100)
    model.fit(x,y)

    new_data = pd.DataFrame([dat])

    fraud_probability = model.predict_proba(new_data)[0][1]
    fr = f"Probability of fraud for this claim: {fraud_probability:.2f}"
    fraud_threshold = 0.7
    if fraud_probability > fraud_threshold:
        return fr , "Hence, this claim is flagged as potentially fraudulent."
    else:
        return fr , "Hence, this claim seems likely to be legitimate."