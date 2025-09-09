#To find missing values using Simple Imputer
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
df = pd.read_csv("bank_dataset.csv1.csv")

si=SimpleImputer(strategy="mean")
ar = si.fit_transform(df[["Age","Loan_Amount","Credit_Score"]])
df = pd.DataFrame(ar,columns=["Age","Loan_Amount","Credit_Score"])



null = df.isnull().sum()#isnull for null values , notnull for filled values i.e true or false
print(null)
print(df)