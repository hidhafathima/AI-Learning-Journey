import pandas as pd

df=pd.read_csv("../data/student_data.csv")
X=df[["hours","attendance"]]
y=df["cgpa"]

print(X)
print()
print(y)