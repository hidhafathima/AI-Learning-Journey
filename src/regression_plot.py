import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df=pd.read_csv("../data/student_data.csv")

X=df[["hours"]]
y=df["cgpa"]

model=LinearRegression()
model.fit(X,y)

predicted_cgpa=model.predict(X)
plt.scatter(df["hours"],df["cgpa"])



plt.plot(df["hours"],predicted_cgpa)

plt.xlabel("Hours Studied")
plt.ylabel("CGPA")
plt.title("Hours vs CGPA Regression Line")

plt.show()