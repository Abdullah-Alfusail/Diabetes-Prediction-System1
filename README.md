## README.md

**Diabetes Prediction System**

This project implements a machine learning model to predict the likelihood of diabetes based on patient data.  The system uses a RandomForestClassifier trained on a diabetes dataset.  A user-friendly graphical interface (GUI) built with Tkinter allows users to input patient data and receive a prediction.

**Authors:**

1. Fawaz Faisal Hamod Humaid (202174047)
2. Abdullah ALfusail (201873300)


**Features:**

* **Data Input:**  The GUI provides input fields for relevant patient information (pregnancies, glucose level, blood pressure, skin thickness, insulin level, BMI, diabetes pedigree function, and age).
* **Prediction:** A trained RandomForestClassifier model predicts whether the patient is likely to have diabetes or not.
* **User-Friendly Interface:** The Tkinter GUI makes the system easy to use.
* **Error Handling:**  The system includes error handling to manage invalid input data.
* **Confirmation Screen:** A confirmation screen displays entered data before submission to allow for correction.
* **Detailed Results:**  A detailed result screen provides the prediction in clear Arabic language.


**Technology Stack:**

* **Python:** Programming language.
* **Pandas:** Data manipulation and analysis.
* **NumPy:** Numerical computing.
* **Scikit-learn:** Machine learning library (RandomForestClassifier, StandardScaler, train_test_split).
* **Tkinter:** GUI framework.


**How to Run:**

1. **Prerequisites:** Make sure you have Python installed along with the necessary libraries (pandas, numpy, scikit-learn, tkinter). You can install them using pip:
   ```bash
   pip install pandas numpy scikit-learn
   ```
   Tkinter is usually included with Python installations.

2. **Dataset:** The code expects a CSV file named `diabetes.csv` located at the path specified in `file_path` variable within the python script.  You will need to provide this dataset.

3. **Execution:** Run the `my_project_1.py` script.  This will launch the GUI application.


**Further Development:**

* **Model Improvement:** Explore different machine learning models or techniques to improve prediction accuracy.
* **Data Visualization:** Add data visualization features to better understand the dataset and model performance.
* **Database Integration:** Integrate a database to store patient data and predictions.
* **Deployment:** Deploy the application as a web application for wider accessibility.


**File Structure:**

* `my_project_1.py`: The main Python script containing the code for the diabetes prediction system.
* `diabetes.csv`: The dataset used for training the model (needs to be provided).


This README provides a comprehensive overview of the project.  Remember to replace the placeholder file path with the actual path to your `diabetes.csv` file.
