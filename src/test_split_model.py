import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

# Load data
df=pd.read_csv("../data/student_data.csv")

# Features and target
X=df[["hours","attendance"]]
y=df["cgpa"]

# Split data
X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# Train model
model=LinearRegression()
model.fit(X_train,y_train)

#Predict on unseen students
predictions=model.predict(X_test)

# Evaluate
score=r2_score(y_test,predictions)

print("Test R^2 Score:",score)