import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df=pd.read_csv("../data/student_data.csv")

X=df[["hours","attendance"]]

y=df["cgpa"]

model=LinearRegression()

model.fit(X,y)

joblib.dump(model, "../models/cgpa_model.pkl")

print("Model trained and saved successfully!")

