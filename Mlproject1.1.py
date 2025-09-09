#Encoding using One hot encoder
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
df = pd.read_csv("bank_dataset.csv.csv")
print(df.head(3))
df["Gender"].fillna(df["Gender"].mode()[0],inplace=True)
new_data = df[["Gender"]]
he = OneHotEncoder()
new_data = he.fit_transform(new_data)
ar=new_data.toarray()
ar = pd.DataFrame(ar,columns=["Gender_male" , "Gender_female"])
print(ar)


