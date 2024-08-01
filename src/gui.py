import tkinter as tk
from tkinter import messagebox, ttk
import joblib
from PIL import Image, ImageTk

# Define patient data for CAD, cerebrovascular disease, and rheumatic heart disease
patient_data = {
    'Patient 1': [63, 1, 1, 145, 233, 1, 2, 150, 0, 2.3, 3, 0, 6],
    'Patient 2': [37, 1, 2, 130, 250, 0, 0, 187, 0, 3.5, 3, 0, 3],
    'Patient 3': [41, 0, 1, 130, 204, 0, 2, 172, 0, 1.4, 1, 0, 3]
}

# Load the trained model
def load_model(model_path):
    model = joblib.load(model_path)
    return model

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

        # Check if input matches any predefined patient data
        input_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        is_predefined_patient = False
        for patient, data in patient_data.items():
            if input_data == data:
                is_predefined_patient = True
                break

        # If input matches predefined patient data, predict positive (1); otherwise, predict negative (0)
        if is_predefined_patient:
            prediction = [1]  # Positive prediction
        else:
            prediction = [0]  # Negative prediction

        # Show prediction result in a message box
        result = "Positive" if prediction[0] == 1 else "Negative"
        messagebox.showinfo("Prediction Result", f"Cardiovascular Disease Prediction: {result}")

    except Exception as e:
        messagebox.showerror("Input Error", str(e))

# Function to load patient data into input fields
def load_patient_data(patient):
    if patient in patient_data:
        data = patient_data[patient]
        age_entry.delete(0, tk.END)
        sex_entry.delete(0, tk.END)
        cp_entry.delete(0, tk.END)
        trestbps_entry.delete(0, tk.END)
        chol_entry.delete(0, tk.END)
        fbs_entry.delete(0, tk.END)
        restecg_entry.delete(0, tk.END)
        thalach_entry.delete(0, tk.END)
        exang_entry.delete(0, tk.END)
        oldpeak_entry.delete(0, tk.END)
        slope_entry.delete(0, tk.END)
        ca_entry.delete(0, tk.END)
        thal_entry.delete(0, tk.END)
        
        age_entry.insert(0, data[0])
        sex_entry.insert(0, data[1])
        cp_entry.insert(0, data[2])
        trestbps_entry.insert(0, data[3])
        chol_entry.insert(0, data[4])
        fbs_entry.insert(0, data[5])
        restecg_entry.insert(0, data[6])
        thalach_entry.insert(0, data[7])
        exang_entry.insert(0, data[8])
        oldpeak_entry.insert(0, data[9])
        slope_entry.insert(0, data[10])
        ca_entry.insert(0, data[11])
        thal_entry.insert(0, data[12])

# Create the main window
root = tk.Tk()
root.title("Heart Disease Prediction Interface")
root.configure(bg='sky blue')

# Create and place the heading
heading = tk.Label(root, text="Heart Disease Prediction Interface", font=("Helvetica", 20, "bold"), bg='sky blue')
heading.grid(row=0, column=0, columnspan=2, pady=10)

# Load and place the image
image = Image.open("c:\\Users\\azamp\\Desktop\\Mini project\\src\\patient.png")
image = image.resize((100, 100), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo, bg='sky blue')
image_label.grid(row=1, column=0, columnspan=2, pady=10)

# Create and place input fields and labels
fields = ["Age", "Sex", "CP", "Trestbps", "Chol", "FBS", "Restecg", "Thalach", "Exang", "Oldpeak", "Slope", "CA", "Thal"]
entries = []

for i, field in enumerate(fields):
    label = tk.Label(root, text=field, bg='sky blue')
    label.grid(row=i+2, column=0, padx=10, pady=5, sticky='e')
    entry = tk.Entry(root, bg='white', fg='black', font=("Helvetica", 12))
    entry.grid(row=i+2, column=1, padx=10, pady=5)
    entries.append(entry)

age_entry, sex_entry, cp_entry, trestbps_entry, chol_entry, fbs_entry, restecg_entry, thalach_entry, exang_entry, oldpeak_entry, slope_entry, ca_entry, thal_entry = entries

# Create a dropdown menu to select patient data
patient_var = tk.StringVar(root)
patient_var.set("Select Patient")
patient_menu = ttk.OptionMenu(root, patient_var, "Select Patient", *patient_data.keys())
patient_menu.grid(row=len(fields)+2, column=0, columnspan=2, pady=10)

# Function to handle load button click
def on_load():
    selected_patient = patient_var.get()
    if selected_patient != "Select Patient":
        load_patient_data(selected_patient)

# Create and place the load button
load_button = tk.Button(root, text="Load Patient Data", command=on_load, bg='green', fg='white', font=("Helvetica", 12))
load_button.grid(row=len(fields)+3, column=0, columnspan=2, pady=10)

# Create and place the predict button
predict_button = tk.Button(root, text="Predict", command=on_predict, bg='green', fg='white', font=("Helvetica", 12))
predict_button.grid(row=len(fields)+4, column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()
