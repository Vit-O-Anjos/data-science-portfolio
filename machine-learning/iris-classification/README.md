# Iris Flower Classification with Logistic Regression

## Overview

Advanced multi-class classification project predicting iris flower species using logistic regression. Features comprehensive exploratory data analysis, feature correlation studies, and professional model evaluation with stratified sampling and confusion matrix analysis.

## 🎯 Project Highlights

- **Multi-class Logistic Regression** implementation with 4 morphological features
- **Comprehensive EDA** with pairplots, correlation heatmaps, and feature distribution analysis
- **Stratified Model Evaluation** ensuring representative class distribution
- **Multi-class Metrics** with precision, recall, and F1-score analysis per class
- **Confusion Matrix Analysis** for detailed model performance insights

## 📊 Model Performance

| Metric | Score | Interpretation |
|--------|-------|----------------|
| **Accuracy** | 91.1% | High classification performance |
| **Precision** | 91.6% | Strong positive predictive value |
| **Recall** | 91.1% | Excellent true positive rate |
| **F1-Score** | 91.1% | Balanced precision-recall performance |

### Class-wise Performance
- **Iris-setosa**: 100% across all metrics (perfect classification)
- **Iris-versicolor**: 93.3% recall, 82.4% precision
- **Iris-virginica**: 92.3% precision, 80.0% recall

## 🔧 Technologies & Methods

- **Multi-class Logistic Regression** with scikit-learn
- **Data Preprocessing**: StandardScaler, Label Encoding, Stratified Sampling
- **Model Evaluation**: Accuracy, Precision, Recall, F1-score, Confusion Matrix
- **Data Visualization**: Pairplots, Correlation Heatmaps, Confusion Matrix Display
- **Feature Analysis**: Correlation coefficients, feature importance ranking

## 📈 Key Insights

### Species Classification Patterns
- **Iris-setosa** is perfectly separable with distinct morphological characteristics
- **Iris-versicolor** and **Iris-virginica** show some feature overlap, explaining minor misclassifications
- **Petal measurements** (length and width) are more discriminative than sepal measurements
- Strong positive correlation between petal dimensions and species complexity

### Technical Implementation
- **Stratified sampling** ensures balanced class representation in train/test splits
- **Feature scaling** improves model convergence and performance
- **Multi-class metrics** provide comprehensive performance evaluation
- **Visual analytics** enable intuitive understanding of feature relationships

## 🔍 Feature Correlation Analysis

| Feature | Correlation with Species | Impact |
|---------|--------------------------|--------|
| **Petal Width** | 0.96 (Strong Positive) | Highest discriminative power |
| **Petal Length** | 0.95 (Strong Positive) | Very strong predictor |
| **Sepal Length** | 0.78 (Strong Positive) | Good predictive value |
| **Sepal Width** | -0.42 (Moderate Negative) | Inverse relationship |

## 📊 Results & Visualizations

### Model Performance
![Confusion Matrix](visualizations/confusion_matrix.png)

Confusion matrix showing 91.1% accuracy with perfect setosa classification and 4 misclassifications between versicolor and virginica.

### Feature Relationships
![Pairplot](visualizations/pairplot.png)

Pairplot showing feature distributions and relationships by species, highlighting perfect setosa separation and versicolor-virginica overlap.

### Correlation Analysis
![Correlation Matrix](visualizations/correlation_matrix_full.png)

Feature correlation matrix demonstrating strong relationships between petal measurements and species classification.

### Feature Importance
![Feature Importance](visualizations/feature_importance_correlation.png)

Feature correlation ranking showing petal width (0.96) and length (0.95) have strongest correlation with species.

### Classification Report
![Classification Report](visualizations/classification_report.png)

Detailed performance metrics per class showing 100% setosa accuracy and strong versicolor/virginica performance.

## 💡 Technical Achievements

- **Professional Evaluation**: Stratified train-test split for reliable performance metrics
- **Multi-class Expertise**: Comprehensive metrics beyond simple accuracy
- **Feature Engineering**: Proper scaling and preprocessing pipeline
- **Visual Analytics**: Professional-grade visualizations for model interpretation
- **Model Diagnostics**: Confusion matrix and classification report analysis

## 🏆 Model Excellence

**91.1% Accuracy** - High-performance multi-class classification demonstrating advanced understanding of logistic regression and evaluation methodologies.

## 📁 Dataset

- **Source**: UCI Iris Dataset (classic machine learning benchmark)
- **Samples**: 150 iris flowers
- **Features**: 4 morphological measurements (sepal length, sepal width, petal length, petal width)
- **Classes**: 3 species (Iris-setosa, Iris-versicolor, Iris-virginica)
- **Balance**: Perfectly balanced (50 samples per class)

## 🎯 Business Applications

- **Botanical Research**: Automated species identification and classification
- **Educational Tools**: Machine learning demonstration and teaching
- **Quality Control**: Agricultural and horticultural species verification
- **ML Benchmarking**: Model performance comparison and algorithm testing

## 🚀 Quick Start

### Installation
```bash
pip install -r requirements.txt
