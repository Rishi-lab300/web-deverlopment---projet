#Train , Test and split the dataset into two parts
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
df = pd.read_csv("boston_housing.csv")
print(df.head(3))
input_data = df.iloc[:,:-1]
output_data = df["MEDV"]
x_train,x_test,y_train,y_test = train_test_split(input_data,output_data,test_size=0.25)
print(x_test.shape,x_train.shape)
print(y_test.shape,y_train.shape)