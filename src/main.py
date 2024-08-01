import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from data_preprocessing import load_data, preprocess_data
from src.knn_model import train_knn, evaluate_model, save_model

# Load and preprocess data
file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'heart.csv')
data = load_data(file_path)
X_train, X_test, y_train, y_test = preprocess_data(data)

# Train kNN model
knn = train_knn(X_train, y_train)

# Evaluate the model
evaluate_model(knn, X_test, y_test)

# Save the model
save_model(knn, os.path.join(os.path.dirname(__file__), '..', 'knn_model.pkl'))