import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report

class EmotionDetector:
    def __init__(self, features, labels):
        self.clf = MLPClassifier(hidden_layer_sizes=(128, 64), max_iter=1000)
        self.clf.fit(features, labels)

    def predict(self, features):
        return self.clf.predict(features)

# Load the wearables data
data = pd.read_csv('wearables_data.csv')

# Extract the features
features = data[[ 'heart_rate', 'respiration_rate', 'skin_conductance', 'galvanic_skin_response', 'body_temperature']]

# Extract the labels
labels = data['emotion']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.25, random_state=42)

# Create an emotion detector
detector = EmotionDetector(X_train, y_train)

# Predict the emotions for the test set
y_pred = detector.predict(X_test)

# Evaluate the model performance
print(classification_report(y_test, y_pred))
