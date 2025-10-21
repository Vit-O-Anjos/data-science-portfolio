from setuptools import setup, find_packages

setup(
    name="titanic-survival-prediction",
    version="2.0.0",
    description="Comprehensive ML analysis of Titanic survival prediction with 89.6% accuracy using optimized Decision Trees",
    author="Vitor Anjos", 
    packages=find_packages(),
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "scikit-learn>=1.0.0",
        "matplotlib>=3.5.0", 
        "seaborn>=0.11.0",
        "tabulate>=0.9.0",
    ],
    extras_require={
        "dev": [
            "jupyter>=1.0.0"
        ]
    },
    python_requires=">=3.8",
)
