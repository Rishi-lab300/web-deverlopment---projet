#Remove outliners
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("bank_dataset.csv1.csv")
print(df.head(3))
print("\nUnique ages:", df["Age"].unique()[:20])
q1 = df["Age"].quantile(0.25)


q3 = df["Age"].quantile(0.75)
# Step 2: Calculate IQR
IQR = q3 - q1

# Step 3: Define lower and upper bounds
min_range = q1 - 1.5 * IQR
max_range = q3 + 1.5 * IQR
print("Q1:", q1)
print("Q3:", q3)
print("IQR:", IQR)
print(min_range)
print(max_range)
# Step 4: Filter the DataFrame
df_no_outliers = df[(df["Age"] >= min_range) & (df["Age"] <= max_range)]
df_outliers = df[(df["Age"] < min_range) | (df["Age"] > max_range)]
print("\n✅ Remaining after outlier removal:", df_no_outliers["Age"].value_counts().head())
print("\n🚫 Outliers removed:", df_outliers["Age"].unique())
print(df_no_outliers)
plt.figure(figsize=(15,5))
sns.boxplot(x = "Age" , data = df)
sns.displot(df["Age"])
plt.show()