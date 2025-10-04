# Titanic Survival Prediction with Random Forests

## Overview
Advanced machine learning project predicting passenger survival on the Titanic using Random Forest algorithms. Features comprehensive data preprocessing, hyperparameter optimization, and ensemble method comparisons achieving **84.3% accuracy**.

## 🎯 Project Highlights
- **84.3% Accuracy** on passenger survival prediction
- **Advanced Feature Engineering** with one-hot encoding and missing value imputation
- **Hyperparameter Optimization** using GridSearchCV (444 estimators, max_depth=10)
- **Feature Importance Analysis** identifying fare, age, and sex as key predictors
- **Multiple Ensemble Methods** comparison (Random Forest, Gradient Boosting, Bagging)

## 📊 Model Performance Comparison
| Model | Test Accuracy | Key Features |
|-------|---------------|--------------|
| **Random Forest (Optimized)** | 84.3% | Hyperparameter tuning, feature selection |
| **Gradient Boosting** | 82.8% | Sequential learning |
| **Bagging Classifier** | 85.8% | Ensemble of decision trees |
| **Base Random Forest** | 80.6% | Default parameters |

## 🔧 Technologies & Methods
- **Random Forest Classifier** with ensemble learning
- **GridSearchCV** for hyperparameter optimization
- **Feature Engineering**: One-hot encoding, missing value imputation
- **Model Evaluation**: Accuracy, precision, recall, confusion matrices
- **Feature Importance**: Gini importance analysis
- **Ensemble Methods**: Comparison of multiple algorithms

## 📈 Key Insights
- **Most Important Features**: Fare (26.8%), Age (25.4%), Sex (26.4%)
- **Optimal Parameters**: 444 estimators, max_depth=10, max_features=10
- **Data Quality**: Handled 177 missing age values with mean imputation
- **Model Selection**: Bagging outperformed individual classifiers

text

# Project Structure

random-forests/
├── titanic_survival_prediction.ipynb # Main analysis
├── requirements.txt # Dependencies
├── setup.py # Package configuration
├── .gitignore # File management
└── README.md # Project documentation

text

---

## 🔍 Business Applications

- Risk assessment and survival prediction systems  
- Customer segmentation and targeting  
- Feature importance analysis for decision-making  
- Ensemble method evaluation for model selection  

## 💡 Technical Achievements

- Comprehensive hyperparameter tuning with 960 model evaluations  
- Feature importance visualization using Gini importance  
- Multiple algorithm comparison for optimal model selection  
- Robust data preprocessing pipeline  

## 🏆 Academic Achievement

**Task 21 Score:** 100%  
Perfect score in supervised learning assessment demonstrating advanced Random Forest implementation and optimization techniques.

## 📁 Dataset

- **Source:** Titanic passenger data  
- **Samples:** 891 passengers  
- **Features:** 10 engineered features including Pclass, Age, Fare, Sex, Embarked  
- **Target:** Survival (0 = Did not survive, 1 = Survived)

## 🚀 Quick Start

# Usage

jupyter notebook titanic_survival_prediction.ipynb

### Installation
```bash
pip install -r requirements.txt



