
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import tkinter as tk
from tkinter import messagebox

file_path = "C:/Users/SCC/Desktop/my projec/diabetes.csv" 
data = pd.read_csv(file_path)

X = data.drop('Outcome', axis=1)  
y = data['Outcome']  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train) 
X_test = scaler.transform(X_test)  

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)     


def predict_diabetes(input_data):
    input_data_scaled = scaler.transform(np.array(input_data).reshape(1, -1))
    

    prediction = model.predict(input_data_scaled)
    
    return "مصاب بالسكري" if prediction[0] == 1 else "غير مصاب بالسكري"

def show_detailed_result(result):
    result_window = tk.Toplevel(root)
    result_window.title("نتيجة التحليل")
    
    if result == "مصاب بالسكري":
        result_text = "حسب البيانات المدخلة، التحليل يشير إلى أنك مصاب بالسكري الله يشفيك."
    else:
        result_text = "حسب البيانات المدخلة، التحليل يشير إلى أنك غير مصاب بالسكري ولافيك حاجة روح."
    
    tk.Label(result_window, text=result_text, font=("Arial", 14)).pack(pady=20)
    tk.Button(result_window, text="موافق", command=result_window.destroy).pack(pady=10)


def confirm_data():
    confirm_window = tk.Toplevel(root)
    confirm_window.title("تأكيد البيانات المدخلة")
    
    data_summary = (
        f"عدد مرات الحمل: {entry_pregnancies.get()}\n"
        f"مستوى الجلوكوز: {entry_glucose.get()}\n"
        f"ضغط الدم: {entry_blood_pressure.get()}\n"
        f"سمك الجلد: {entry_skin_thickness.get()}\n"
        f"مستوى الأنسولين: {entry_insulin.get()}\n"
        f"مؤشر كتلة الجسم: {entry_bmi.get()}\n"
        f"تاريخ العائلة للسكري: {entry_diabetes_pedigree.get()}\n"
        f"العمر: {entry_age.get()}\n"
    )
    
    tk.Label(confirm_window, text="يرجى مراجعة البيانات التالية:", font=("Arial", 12)).pack(pady=10)
    tk.Label(confirm_window, text=data_summary, font=("Arial", 10)).pack(pady=10)
    tk.Button(confirm_window, text="تأكيد", command=lambda: [submit_data(), confirm_window.destroy()]).pack(pady=10)
    tk.Button(confirm_window, text="تعديل", command=confirm_window.destroy).pack(pady=10)

def submit_data():
    try:
        pregnancies = int(entry_pregnancies.get())
        glucose = float(entry_glucose.get())
        blood_pressure = float(entry_blood_pressure.get())
        skin_thickness = float(entry_skin_thickness.get())
        insulin = float(entry_insulin.get())
        bmi = float(entry_bmi.get())
        diabetes_pedigree = float(entry_diabetes_pedigree.get())
        age = int(entry_age.get())
        
        new_patient_data = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]
        
        result = predict_diabetes(new_patient_data)
        
        show_detailed_result(result)
    except ValueError:
        messagebox.showerror("خطأ", "يرجى إدخال قيم صحيحة.")

def show_data_entry():
    tk.Label(root, text="عدد مرات الحمل:").grid(row=0, column=0)
    global entry_pregnancies
    entry_pregnancies = tk.Entry(root)
    entry_pregnancies.grid(row=0, column=1)

    tk.Label(root, text="مستوى الجلوكوز:").grid(row=1, column=0)
    global entry_glucose
    entry_glucose = tk.Entry(root)

    entry_glucose.grid(row=1, column=1)

    tk.Label(root, text="ضغط الدم:").grid(row=2, column=0)
    global entry_blood_pressure
    entry_blood_pressure = tk.Entry(root)
    entry_blood_pressure.grid(row=2, column=1)

    tk.Label(root, text="سمك الجلد:").grid(row=3, column=0)
    global entry_skin_thickness
    entry_skin_thickness = tk.Entry(root)
    entry_skin_thickness.grid(row=3, column=1)

    tk.Label(root, text="مستوى الأنسولين:").grid(row=4, column=0)
    global entry_insulin
    entry_insulin = tk.Entry(root)
    entry_insulin.grid(row=4, column=1)

    tk.Label(root, text="مؤشر كتلة الجسم (BMI):").grid(row=5, column=0)
    global entry_bmi
    entry_bmi = tk.Entry(root)

    entry_bmi.grid(row=5, column=1)

    tk.Label(root, text="تاريخ العائلة للسكري:").grid(row=6, column=0)
    global entry_diabetes_pedigree
    entry_diabetes_pedigree = tk.Entry(root)
    entry_diabetes_pedigree.grid(row=6, column=1)

    tk.Label(root, text="العمر:").grid(row=7, column=0)
    global entry_age
    entry_age = tk.Entry(root)
    entry_age.grid(row=7, column=1)

    btn_submit = tk.Button(root, text="تحليل", command=confirm_data)
    btn_submit.grid(row=8, columnspan=2)

def show_welcome_screen():
    welcome_window = tk.Toplevel(root)
    welcome_window.title("أهلاً بك")

    
    tk.Label(welcome_window, text="أهلاً بك في عيادة طوفان الاقصى لفحص مرض السكري مجاناً", font=("Arial", 16)).pack(pady=20)
    tk.Button(welcome_window, text="ابدأ", command=lambda: [welcome_window.destroy(), show_data_entry()]).pack(pady=10)

root = tk.Tk()
root.title("توقع مرض السكري")

show_welcome_screen()

root.mainloop()
