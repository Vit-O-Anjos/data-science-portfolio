from setuptools import setup, find_packages

setup(
    name="mnist-digit-classification",
    version="1.0.0",
    description="Advanced Random Forest for MNIST handwritten digit classification with image preprocessing",
    author="Vitor Anjos",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0", 
        "matplotlib>=3.5.0",
        "seaborn>=0.11.0",
        "scikit-learn>=1.0.0",
        "scikit-image>=0.19.0",
    ],
    extras_require={
        "dev": [
            "jupyter>=1.0.0"
        ]
    },
    python_requires=">=3.8",
)
