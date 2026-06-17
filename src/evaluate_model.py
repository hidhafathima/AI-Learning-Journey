import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load data
df=pd.read_csv("../data/student_data.csv")

#  Features
X=df[["hours","attendance"]]

# Target
y=df["cgpa"]

# Train model
model=LinearRegression()
model.fit(X,y)

# Predictions=model.predict(X)

# Predictions on training data
predictions=model.predict(X)

# Calculate R^2 score
score=r2_score(y,predictions)

print("R^2 Score:",score)