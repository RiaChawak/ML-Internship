
#Author: Ria Chawak

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

data = pd.read_csv('Churn_Modelling.csv')

print(data.head())

X = data.iloc[:, 3:13]
y = data.iloc[:, 13]

label_encoder_X = LabelEncoder()
X['Geography'] = label_encoder_X.fit_transform(X['Geography'])
X['Gender'] = label_encoder_X.fit_transform(X['Gender'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

def train_model(model, X_train, y_train, X_test, y_test):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

print("\nLogistic Regression:")
log_reg = LogisticRegression(random_state=0)
train_model(log_reg, X_train, y_train, X_test, y_test)

print("\nRandom Forest:")
random_forest = RandomForestClassifier(n_estimators=100, random_state=0)
train_model(random_forest, X_train, y_train, X_test, y_test)

print("\nGradient Boosting:")
gradient_boosting = GradientBoostingClassifier(n_estimators=100, random_state=0)
train_model(gradient_boosting, X_train, y_train, X_test, y_test)

df = pd.read_csv('Churn_Modelling.csv')
print(df.head())

X = df.iloc[:, 3:13]  #  columns 3 to 12
y = df.iloc[:, 13]    # column 13 (Exited)

labelencoder_X = LabelEncoder()
X['Geography'] = labelencoder_X.fit_transform(X['Geography'])
X['Gender'] = labelencoder_X.fit_transform(X['Gender'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

classifier = RandomForestClassifier(n_estimators=100, criterion='entropy', random_state=0)
# classifier = LogisticRegression()
# classifier = XGBClassifier()

# Fit the classifier to the training data
classifier.fit(X_train, y_train)

# Predict the Test set results
y_pred = classifier.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
