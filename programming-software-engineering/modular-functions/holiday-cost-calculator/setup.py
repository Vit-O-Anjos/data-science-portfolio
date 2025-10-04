"""
Holiday Cost Calculator Setup
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="holiday-cost-calculator",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Modular holiday cost calculator with robust input validation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/your-repo/tree/main/programming-software-engineering/modular-functions/holiday-cost-calculator",
    py_modules=["holiday_calculator"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.6",
    # No install_requires since no external dependencies
)
