
# 📊 Student Performance Prediction

This project aims to predict students' final exam scores using various lifestyle and academic factors such as study hours, attendance, and extracurricular activities. The model helps identify patterns that contribute to better academic performance.

---

## 🚀 Project Summary

A regression-based machine learning pipeline that:

- Loads and cleans the dataset
- Handles missing values and categorical data
- Performs exploratory data analysis (EDA)
- Trains a regression model to predict final scores
- Evaluates model performance using appropriate metrics

---

## 📁 Dataset

The dataset (`xyz.csv`) contains the following features:

- `study_hours/week`
- `attendance`
- `extracurricular_activities` (categorical: Low, Moderate, High)
- `sleep_hours`
- `final_score` (target variable)

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn

---

## 📊 EDA Highlights

- Distribution plots of features
- Correlation heatmap
- Box plots to detect outliers

---

## 🤖 ML Approach

- **Preprocessing**: Missing value handling, feature encoding, normalization
- **Model Used**: Linear Regression (can be extended to others)
- **Evaluation Metrics**: 
  - Mean Squared Error (MSE)
  - Root Mean Squared Error (RMSE)
  - R² Score

---

## 📈 Results

- The model shows a decent predictive capability based on study time and other lifestyle variables.
- Feature importance analysis suggests that `study_hours/week` and `attendance` are the most impactful.

---

## ✅ Future Work

- Implement classification to categorize students into grade bands
- Include more features like parental education, socioeconomic status
- Improve performance using ensemble models

---

## 🤝 Contributions

Feel free to fork this repo and submit pull requests for enhancements or new models!

---

## 📬 Contact

Created by [Bishal Giri](https://github.com/bishal-777) and [Manu Sharan Sah](https://github.com/manusharansah) - feel free to connect!
