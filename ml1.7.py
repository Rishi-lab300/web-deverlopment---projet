#Function Transformer
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import FunctionTransformer
data = {"Numbers":[1,2,54,67,+3,54,76]}
df = pd.DataFrame(data)
df = df.replace("+3","3").astype("int64")
print(df.info())

dataset = pd.read_csv("bank_dataset1.csv")
ft = FunctionTransformer(func=lambda x:x**2)
dataset["CoapplicantIncome_tf"] = ft.fit_transform(dataset[["CoapplicantIncome"]])
 
sns.displot(dataset["CoapplicantIncome_tf"],kde = True)
plt.show()