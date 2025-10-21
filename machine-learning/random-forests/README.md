# Titanic Survival Prediction - Comprehensive ML Analysis

## 🎯 Project Overview
Advanced machine learning project predicting passenger survival on the Titanic using comprehensive analysis of multiple algorithms. Features systematic model comparison, pruning strategies, and ensemble method evaluation, with **89.6% accuracy** achieved through optimized Decision Tree.

## 🏆 Key Achievements
- **Best Model Accuracy**: 89.6% (Pre-pruned Decision Tree)
- **Critical Insight**: Proper single-model tuning outperforms complex ensembles
- **Optimal Parameters**: max_depth=7, min_samples_leaf=6, entropy criterion
- **Key Features**: Fare, Age, Sex identified as primary predictors

## 📊 Model Performance Comparison

| Model                         | Test Accuracy | Key Features           |
|-------------------------------|---------------|-----------------------|
| **Decision Tree (Pre-Pruned)**| **89.6%** 🥇  | max_depth=7, entropy criterion |
| Post-Pruning (Systematic)      | 86.6% 🥈      | Alpha=0.005           |
| Post-Pruning (CV)              | 86.6% 🥈      | Cross-validated alpha selection |
| Bagging Classifier             | 85.8% 🥉      | 50 estimators         |
| Optimized Random Forest        | 84.3%         | Hyperparameter tuning |
| Gradient Boosting              | 82.8%         | Sequential learning   |
| Random Forest (Base)           | 80.6%         | Default parameters    |
| Decision Tree (Unpruned)       | 76.1%         | Overfit baseline      |

## 🔧 Technologies & Methods

### Core Algorithms
- **Decision Trees** with comprehensive pruning analysis
- **Ensemble Methods**: Random Forest, Gradient Boosting, Bagging
- **Hyperparameter Optimization**: GridSearchCV, systematic depth testing
- **Model Validation**: Cross-validation, train/test/validation splits

### Advanced Techniques
- **Pre-pruning**: Maximum depth optimization
- **Post-pruning**: Cost-complexity pruning with alpha selection
- **Feature Importance**: Gini importance analysis
- **Model Interpretation**: Tree visualization and decision path analysis

## 📈 Key Insights & Findings

### 🎯 Best Performing Strategy
**Pre-pruned Decision Tree (max_depth=7)** achieved superior performance, demonstrating that:  
- Proper single-model tuning can outperform complex ensembles  
- Systematic depth analysis (1-10) revealed optimal complexity at depth 7  
- Train-test gap minimized to 0.6% indicating excellent generalization

### 🔍 Critical Features  
1. **Fare** (26.8% importance) - Strongest predictor of survival  
2. **Age** (25.4% importance) - Key demographic factor  
3. **Sex** (26.4% combined importance) - Critical evacuation priority

### 📊 Pruning Strategy Analysis
- **Pre-pruning**: 89.6% accuracy (optimal balance)  
- **Post-pruning V1**: 86.6% (systematic alpha testing)  
- **Post-pruning V2**: 86.6% (cross-validated alpha selection)

## 📁 Dataset Features

### Original Features
- PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked

### Engineered Features (10 total)
- Pclass, Age, SibSp, Parch, Fare  
- Sex_female, Sex_male (one-hot encoded)  
- Embarked_C, Embarked_Q, Embarked_S (one-hot encoded)

### Data Quality
- **Samples**: 891 passengers  
- **Missing Values**: 177 Age values handled with mean imputation  
- **Target**: Survival (0 = Did not survive, 1 = Survived)

## Key Code Sections
- Data Preprocessing: Missing value handling, feature engineering  
- Model Training: Multiple algorithm implementation  
- Pruning Analysis: Comprehensive depth and alpha testing  
- Model Evaluation: Accuracy metrics, confusion matrices, feature importance

## 📊 Key Visualizations

### 1. Model Performance Comparison
![Model Comparison](visualizations/model_comparison_chart.png)

*Pre-pruned Decision Tree (89.6%) outperformed all ensemble methods*

### 2. Optimal Depth Analysis  
![Pruning Analysis](visualizations/pruning_analysis_depth.png)

*Systematic depth testing revealed optimal performance at depth=7*

### 3. Best Model Performance
![Confusion Matrix](visualizations/best_model_confusion_matrix.png)

*89.6% accurate pre-pruned Decision Tree confusion matrix*

### 4. Feature Importance
![Feature Importance](visualizations/feature_importance_plot.png)

*Fare, Age, and Sex identified as most predictive features*

---

## 🔍 Technical Analysis Visualizations

### Cost-Complexity Pruning Analysis
![Post-Pruning Analysis](visualizations/cost_complexity_pruning.png)

*Alpha parameter optimization for post-pruning strategies*

### Decision Tree Structure
![Tree Structure](visualizations/decision_tree_structure.png)

*Optimal depth=7 Decision Tree visualization*

### Feature Correlations
![Correlation Heatmap](visualizations/correlation_heatmap.png)

*Feature relationships and multicollinearity analysis*

## 🔍 Business & Historical Context  
The model's findings validate known historical patterns:  
- Higher fare passengers (likely higher class) had better survival chances  
- "Women and children first" policy reflected in Sex and Age importance  
- Family size (SibSp, Parch) influenced survival outcomes

## 💡 Technical Achievements  
- Systematic Model Comparison: 7 different algorithms evaluated  
- Comprehensive Pruning Analysis: Multiple strategies compared  
- Feature Importance Validation: Historical accuracy of identified predictors  
- Robust Validation: Triple split (train/test/validation) with cross-validation

## 🎓 Academic Excellence  
Perfect Score Achievement demonstrating:  
- Advanced understanding of tree-based algorithms  
- Comprehensive model evaluation methodology  
- Effective hyperparameter optimization strategies  
- Insightful interpretation of machine learning results

## 📈 Project Evolution  
This project evolved from basic Random Forest implementation to comprehensive machine learning analysis, revealing that:  
- Model simplicity with proper tuning can outperform complexity  
- Systematic experimentation is crucial for optimal performance  
- Domain knowledge integration enhances model interpretability

*Demonstrating that in machine learning, sometimes the most elegant solution is also the most effective.*

## 🚀 Quick Start

### Installation
```bash
pip install -r requirements.txt

# Usage

jupyter notebook titanic_survival_prediction.ipynb




