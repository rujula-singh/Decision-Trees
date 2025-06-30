
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier, plot_tree  # Changed here
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("./heart.csv")
print("Dataset loaded successfully!")

# Data preprocessing
print("\nData Preprocessing:")
print("Initial shape:", df.shape)

# Handle missing values
df = df.dropna()
print("\nMissing values after handling:")
print(df.isnull().sum())

# Convert target to binary if needed
if len(df['target'].unique()) > 2:
    df['target'] = df['target'].apply(lambda x: 0 if x == 0 else 1)

# Separate features and target
X = df.drop('target', axis=1)
y = df['target']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print("\n1. Decision Tree Classifier:")
dt_clf = DecisionTreeClassifier(random_state=42)
dt_clf.fit(X_train, y_train)

# Visualize with matplotlib
plt.figure(figsize=(20,10))
plot_tree(dt_clf, 
          feature_names=X.columns, 
          class_names=['No Disease', 'Disease'],
          filled=True,
          rounded=True)
plt.savefig('decision_tree.png', dpi=300, bbox_inches='tight')
print("Decision tree visualization saved as decision_tree.png")
plt.show()

# Evaluate
y_pred = dt_clf.predict(X_test)
print("\nDecision Tree Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
