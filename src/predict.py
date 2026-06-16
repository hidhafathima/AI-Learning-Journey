import joblib
import pandas as pd

model=joblib.load("../models/cgpa_model.pkl")

input_data=pd.DataFrame([[8,95]],columns=["hours","attendance"])

prediction=model.predict(input_data)

print("Predicted CGPA:",prediction[0])