import tkinter as tk
from tkinter import messagebox
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the trained model
def load_model(model_path):
    model = joblib.load(model_path)
    return model

# Function to preprocess input data
def preprocess_data(input_data):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(input_data)
    return scaled_data

# Function to predict using the loaded model
def predict(model, input_data):
    prediction = model.predict(input_data)
    return prediction

# Function to handle button click (predict)
def on_predict():
    try:
        # Get user input
        age = float(age_entry.get())
        sex = float(sex_entry.get())
        cp = float(cp_entry.get())
        trestbps = float(trestbps_entry.get())
        chol = float(chol_entry.get())
        fbs = float(fbs_entry.get())
        restecg = float(restecg_entry.get())
        thalach = float(thalach_entry.get())
        exang = float(exang_entry.get())
        oldpeak = float(oldpeak_entry.get())
        slope = float(slope_entry.get())
        ca = float(ca_entry.get())
        thal = float(thal_entry.get())

        # Create DataFrame from user input
        input_data = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]],
                                  columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'])

        # Preprocess input data
        input_data_scaled = preprocess_data(input_data)

        # Load the model and make prediction
        model_path = 'knn_model.pkl'  # Adjust path if necessary
        model = load_model(model_path)
        prediction = predict(model, input_data_scaled)

        # Show prediction result in a message box
        result = "Positive" if prediction[0] == 1 else "Negative"
        messagebox.showinfo("Prediction Result", f"Cardiovascular Disease Prediction: {result}")

    except Exception as e:
        messagebox.showerror("Input Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Cardiovascular Disease Prediction")

# Create and place input fields and labels
fields = ["Age", "Sex", "CP", "Trestbps", "Chol", "FBS", "Restecg", "Thalach", "Exang", "Oldpeak", "Slope", "CA", "Thal"]
entries = []

for i, field in enumerate(fields):
    label = tk.Label(root, text=field)
    label.grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

age_entry, sex_entry, cp_entry, trestbps_entry, chol_entry, fbs_entry, restecg_entry, thalach_entry, exang_entry, oldpeak_entry, slope_entry, ca_entry, thal_entry = entries

# Create and place the predict button
predict_button = tk.Button(root, text="Predict", command=on_predict)
predict_button.grid(row=len(fields), column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()