#removing outliners by z_score
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("bank_dataset.csv1.csv")
print(df.head(3))

data = df["Loan_Amount"]

z_score = (df["Loan_Amount"] - df["Loan_Amount"].mean()) / (df["Loan_Amount"].std())
df["z_score"] = z_score
print(df)
sns.boxplot(x = "Loan_Amount",data = df)
sns.displot(df["Loan_Amount"])
plt.show()