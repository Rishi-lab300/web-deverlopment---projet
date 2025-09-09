#Multi linear regression
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df = pd.read_csv("age_dataset.csv")
print(df.shape)
x = df.iloc[:,:-1]
y = df["Salary"]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
lr = LinearRegression()
lr = lr.fit(x_train,y_train)
print("Accuracy: " , lr.score(x_test,y_test)*100)
print("Coeffiecient:",lr.coef_)
print(lr.intercept_)
#formula used  = y*m1x1+m2x2+c = 1934.12295022*Age-25252.58861671*experience+30189.880023633537
y_prd = lr.predict(x_test)
print(y_prd)#to predict the e
#sns.pairplot(data=df)
sns.heatmap(data=df.corr(),annot=True)
plt.show()