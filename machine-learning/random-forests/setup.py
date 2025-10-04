from setuptools import setup, find_packages

setup(
    name="titanic-survival-prediction",
    version="1.0.0",
    description="Advanced Random Forest for Titanic survival prediction with feature importance analysis",
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
