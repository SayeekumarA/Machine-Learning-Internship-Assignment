# 🧠 Understanding Human-Emotional State

This project builds a machine learning system that understands user emotions from journal text and suggests what the user should do and when.

---

## ⚙️ Setup Instructions

1. Install required libraries:
   pip install pandas numpy scikit-learn matplotlib

2. Place the files:
   - training_data.xlsx
   - testing_data.xlsx

3. Open the notebook:
   ML_Project.ipynb

4. Run all cells step by step

---

## 🧠 Approach

The system works in 3 main steps:

1. Understand emotion from text  
2. Predict how strong the emotion is (intensity)  
3. Suggest what action the user should take and when  

---

## 🔧 Feature Engineering

We used two types of features:

### 1. Text Features
- Used TF-IDF (Term Frequency - Inverse Document Frequency)
- Converts text into numbers
- Captures important words and phrases

### 2. Metadata Features
- sleep_hours
- stress_level
- energy_level
- time_of_day
- ambience_type
- previous_day_mood
- face-emotion hint
- reflection quality

These are scaled using StandardScaler

---

## 🤖 Model Choice

We used:

### Emotional State (Classification)
- Model: Linear SVM (LinearSVC)
- Reason: Works well for text classification

### Intensity (Regression)
- Model: Ridge Regression
- Reason: Simple and stable for numeric prediction

---

## ⚡ How to Run

1. Train model using training dataset  
2. Generate predictions on test dataset  
3. Run decision engine  
4. Create final predictions.csv  

Output includes:
- predicted_state  
- predicted_intensity  
- confidence  
- uncertain_flag  
- what_to_do  
- when_to_do
- supportive_message  

---

## 📊 Output Example

State: focused  
Intensity: 3  
Action: deep_work  
When: now  

---

## 📌 Note

Test dataset does not have labels, so evaluation metrics like accuracy and MSE are calculated only on training data. 
