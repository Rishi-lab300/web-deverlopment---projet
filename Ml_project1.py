#Fill all the missing values in Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("bank_dataset.csv1.csv")
null = df.isnull().sum()#isnull for null values , notnull for filled values i.e true or false
print(null)
#df = df.fillna(10)
#print(df)

'''df = df.fillna(method = "ffill")#ffill for foward , bfill for backward
print(df)
df = df.fillna(method = "ffill" , axis = 1)#ffill for foward , bfill for backward i.e columns
print(df)
df = df[i].mode()[0]'''


for i in df.select_dtypes(include=object).columns:
    df[i] = df[i].fillna(df[i].mode()[0])
    print(df[i])
for i in df.select_dtypes(include="Float64").columns:
    df[i] = df[i].fillna(df[i].mode()[0])
    print(df[i])
null = df.isnull().sum()#isnull for null values , notnull for filled values i.e true or false
print(null)





