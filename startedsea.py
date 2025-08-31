# Install (if not already installed)
# pip install seaborn
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Create some data
data = np.random.randn(1000)

# Histogram
sns.histplot(data, bins=30, color="skyblue", kde=True)
plt.show()

# Fake dataset
x = np.random.rand(50)
y = np.random.rand(50)

# Scatter plot
sns.scatterplot(x=x, y=y, color="red", marker="o")
plt.show()
# Load dataset
tips = sns.load_dataset("tips")

# Scatter with color by gender
sns.scatterplot(x="total_bill", y="tip", hue="sex", data=tips)
plt.show()
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title("Ex4: Boxplot")
plt.show()
sns.pairplot(tips, hue="sex")
plt.show()

tips = sns.load_dataset('tips')
data = tips['tip'].mean()
sns.barplot(x="day",y="tip",hue="sex",data=tips,palette="Set2")
plt.xlabel("Day of Week")
plt.ylabel("Average Tip")
plt.legend(title="Gender")
plt.show()



tips = sns.load_dataset("tips")
corr = tips.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

data = np.random.randn(1000)

sns.kdeplot(x=data, color="red", fill=True)  # <-- x=data instead of data
plt.title("KDE Plot")
plt.show()
sns.rugplot(data, color="black")
plt.title("Rug Plot")
plt.show()
sns.countplot(x="day", data=tips, palette="pastel")
plt.title("Countplot - Count per Day")
plt.show()
sns.violinplot(x="day", y="total_bill", data=tips, palette="muted")
plt.title("Violinplot - Total Bill by Day")
plt.show()
sns.stripplot(x="day", y="total_bill", data=tips, jitter=True, palette="Set1")
plt.title("Stripplot - Total Bill by Day")
plt.show()
sns.swarmplot(x="day", y="total_bill", data=tips, palette="Dark2")
plt.title("Swarmplot - Total Bill by Day")
plt.show()
sns.lmplot(x="total_bill", y="tip", hue="sex", data=tips)
plt.show()
sns.catplot(x="day", y="total_bill", hue="sex", kind="bar", data=tips)
plt.show()