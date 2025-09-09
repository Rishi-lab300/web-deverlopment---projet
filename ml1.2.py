#Label encoding
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv("bank_dataset.csv.csv")
print(df.head(3))
la = LabelEncoder()
df["Branch"] = la.fit_transform(df["Branch"])
print(df["Branch"])
unique = df["Branch"].unique()
print(unique)
from sklearn.preprocessing import OrdinalEncoder
ds = pd.DataFrame({"Size" :["s",'m',"l","xl","s","m","l","xl","s","s","l","xl"]})
print(ds)
data = [["s","m","l","xl"]]
oe = OrdinalEncoder(categories=data)
oe = oe.fit_transform(ds[["Size"]])
print(oe)