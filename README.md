# 🧠 Project Title

> Predicting Heart Disease Using Supervised Machine Learning Algorithms

---

## 📌 Problem Statement

- Heart Disease is a leading cause of Death globally. Predicting it early can save lives by enabling timely medical intervention.
- It affects all ages of people, especially those with poor lifestyle habits, genetical risks and existing medical conditions.
- The project aims to predict whether a person is at risk of developing heart disease based on demographic and medical features.

---

## 📂 Project Structure

```
heart-disease-ml-project/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── heart.csv
├── model/
│   └── svc_final_pipeline.pkl
├── notebooks/
│   ├── heart_disease_prediction.ipynb
│   └── images/
```

---

## 📊 Dataset

- **Source**: [Kaggle](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)
- **Number of Rows**: 1025
- **Number of Features**: 14
- **Target Variable**: `HeartDisease(Yes/No)`
- **Missing Values**: None found
- **Duplicates**: Found and removed
- **Feature Types**: Separated into categorical and numerical for preprocessing
- **Class Distribution**: Balanced (1 is aprox 54% and 0 is 46%)

---

## ⚙️ Methodology

- Data Loading and Initial Inspection
- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Checking Outliers and Skewness
- Supervised Machine Learning Models: Training and Evaluation
- Deployment

---

## 📈 Data Preprocessing

- No missing values were found in the dataset.
- Detected and removed duplicate records.
- Separated features into categorical and numerical columns for better handling.
- Confirmed that the target variable is balanced.

---

## 📈 Exploratory Data Analysis (EDA)

- Analyzed the distribution of the `target variable` using histograms.
- Examined the distribution of `numerical features` with histograms to understand their spread and detect potential outliers.
- Visualized the distribution of `categorical variables` using count plots to assess class balance and frequency.
- Visualized barplots to explore the relationship between categorical features and the target variable. Observed that certain categories have a higher proportion of positive cases, indicating potential predictive power.
- Computed correlation among `numerical features` and found no significant multicollinearity.
- Visualized correlations using a heatmap for better interpretation.

---

## 📈 Checking Outliers and Skewness

- Used boxplots to visualize `numerical features` for potential outliers and identified outliers in some variables.
- Calculated skewness values for `numerical features` using `scipy.stats` library and detected some features are slighly positive skewed.

---

## 📈 Supervised Machine Learning Models: Training and Evaluation

📌 Models Trained:

- Logistic Regression
- Support Vector Classifier (SVC)
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost
- LGTBoost
- CatBoost

---

**Training and evaluation were done using:**

- train_test_split (80% train / 20% test)
- accuracy_score on test data
- GridSearchCV for hyperparameter tuning (on best models)

---

**🏆 Best Performing Models (Based on Cross-Validation Score)**
| Model | CV Accuracy | Test Accuracy |
| ----------------- | ----------- | ------------- |
| **SVC** | 0.849 | 0.8026 |
| **Random Forest** | 0.845 | 0.8026 |

---

## 📌 Key Insights

- Support Vector Classifier (SVC) performed best based on cross-validation accuracy (0.849), slightly outperforming Random Forest (0.845). Despite similar test accuracy (0.8026), SVC was chosen for deployment due to its better generalization, simplicity, and consistency across folds.

---

## 🖥️ Web Application

This project includes a user-friendly Streamlit web app that allows users to input personal health information and receive:

- Prediction: Whether the user is likely to have heart disease (Yes/No)
- Probability: The model's confidence score for the prediction

---

**🔍 Features**

- Real-time input form with dropdowns and number fields
- Displays both prediction and probability instantly
- Fully powered by a trained SVC model with preprocessing pipeline

---

## 💡 Future Work

- Use more data or external datasets
- Try ensemble models or deep learning

---

## 🚀 How to Run the App Locally

- Step 1: Activate your virtual environment (if any)
- Step 2: Install required packages
  pip install -r requirements.txt
- Step 3: Run the Streamlit app
  streamlit run app.py
  After running the above command, the app will open in your browser at http://localhost:8501/.

---

## 🙋‍♂️ Author

**Md. Hasib** <br>
_BSc Statistics Student, University of Chittagong_ <br>
Email: mdhasib.stats@gmail.com <br>
GitHub: [@mdhasibstats](https://github.com/mdhasibstats)  
LinkedIn: [mdhasib-statistics](https://linkedin.com/in/mdhasib-statistics)

---
