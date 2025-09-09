#backward and forward elimination using scikit learn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
df = pd.read_csv("diabetes_dataset.csv")
print(df.head(3))
x= df.iloc[:,:-1]
y= df["Outcome"]
print(x.shape)
lr = LogisticRegression()
fs = SequentialFeatureSelector(lr,n_features_to_select = 4,direction="forward")#if want backward write backward
fs = fs.fit(x,y)
selected_features = (x.columns[fs.get_support()]) 
print("Selected_features" , selected_features)
scores = cross_val_score(lr, x[selected_features], y, cv=5, scoring="accuracy")
print("Cross-validation accuracy:", scores.mean())
#backward and forward elimination using mlxtend
'''from sklearn.linear_model import LogisticRegression
from mlxtend.feature_selection import SequentialFeatureSelector

fs = SequentialFeatureSelector(lr,
                               k_features=4,       # choose 4 best features
                               forward=True,       # forward selection
                               scoring='accuracy', # evaluation metric
                               cv=5)               # 5-fold cross-validation

fs = fs.fit(x, y)

# Results
print("Selected Features:", fs.k_feature_names_)  # names of selected features
print("CV Accuracy of Selected Subset:", fs.k_score_)  # mean cross-val score'''