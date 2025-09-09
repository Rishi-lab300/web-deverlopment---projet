#To find and remove duplicates froom the dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("bank_dataset1.csv")
print(df.shape)
print(df.drop_duplicates())
print(df.shape)