
#  Heart Disease Prediction using Decision Tree & Random Forest

This project applies machine learning techniques like **Decision Trees** and **Random Forests** to predict the presence of heart disease using clinical features.

It performs a full pipeline:
- Importing and cleaning the dataset
- Handling missing values
- Training a model
- Evaluating performance
- Visualizing a decision tree


##  Dataset

- File used: `heart.csv`
- Each row is a patient record
- Target column: `target` (0 = No Disease, 1 = Disease)


##  Features Used

| Feature Name   | Description                                 |
|----------------|---------------------------------------------|
| age            | Age in years                                |
| sex            | Gender (1 = male, 0 = female)               |
| cp             | Chest pain type (0–3)                       |
| trestbps       | Resting blood pressure (in mm Hg)           |
| chol           | Serum cholesterol (mg/dl)                   |
| fbs            | Fasting blood sugar > 120 mg/dl (1 = true)  |
| restecg        | Resting ECG results                         |
| thalach        | Maximum heart rate achieved                 |
| exang          | Exercise induced angina (1 = yes, 0 = no)   |
| oldpeak        | ST depression induced by exercise           |
| slope          | Slope of the ST segment                     |
| ca             | Major vessels colored by fluoroscopy (0–3)  |
| thal           | Thalassemia: 3 = normal, 6 = fixed, 7 = reversible |
| target         | 0 = No Disease, 1 = Disease (binary)        |
