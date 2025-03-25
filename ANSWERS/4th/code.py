import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

dataframe = pd.read_csv("C:/Users/user/Desktop/ALL INTERNSHIPS (IMP)/4) CODTECH (30jan-30mar)/ANSWERS/4th/spam.csv", encoding="latin-1")

dataframe.columns = ["label", "text"]

label_encoder = LabelEncoder()
dataframe["label"] = label_encoder.fit_transform(dataframe["label"])

print("Class distribution:\n", dataframe["label"].value_counts())

x = dataframe["text"]
y = dataframe["label"]

test_size = 0.2 if len(dataframe) > 100 else 0.3
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=42, stratify=y)

cv = CountVectorizer()
x_train_features = cv.fit_transform(x_train)
x_test_features = cv.transform(x_test)

tuned_parameters = {"kernel": ["linear", "rbf"], "gamma": [1e-3, 1e-4], "C": [1, 10, 100, 1000]}

model = GridSearchCV(svm.SVC(), tuned_parameters, cv=2)

model.fit(x_train_features, y_train)

print("Best Parameters:", model.best_params_)

best_model = svm.SVC(C=model.best_params_["C"], gamma=model.best_params_["gamma"], kernel=model.best_params_["kernel"])
best_model.fit(x_train_features, y_train)

y_pred = best_model.predict(x_test_features)

print("\nModel Evaluation:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred, zero_division=1))

print("\nSample Predictions:")
for i in range(min(5, len(y_test))):
    print(f"Text: {x_test.iloc[i]}\nActual: {y_test.iloc[i]}, Predicted: {y_pred[i]}\n")