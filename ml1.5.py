#Scaling using Standard scalar and normalization minmaxscalar
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
df = pd.read_csv("bank_dataset1.csv")
print(df.head(3))
null = df.isnull().sum()
print(null)
sns.displot(df["ApplicantIncome"])
print(df.describe())

ss = StandardScaler()
ss = ss.fit(df[["ApplicantIncome"]])
df["ApplicantIncome_ss"] = pd.DataFrame(ss.transform(df[["ApplicantIncome"]]),columns=["x"])
print(df.head(3))
print(df.describe())

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.title("before ")
sns.histplot(df["ApplicantIncome"])
plt.subplot(1,2,2)
plt.title("After")
sns.histplot(df["ApplicantIncome"])
plt.show()
from sklearn.preprocessing import MinMaxScaler
ms = MinMaxScaler()
ms = ms.fit(df[["CoapplicantIncome"]])
df["CoapplicantIncome_min"] = ms.transform(df[["CoapplicantIncome"]])
sns.histplot(df["CoapplicantIncome_min"])
plt.show()