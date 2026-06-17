import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df=pd.read_csv("../data/student_data.csv")

# Scatter plot
plt.scatter(df["hours"],df["cgpa"])

# Labels
plt.xlabel("Hours Studied")
plt.ylabel("CGPA")
plt.title("Hours Studied vs CGPA")

print(df[["hours", "cgpa"]])

plt.show()