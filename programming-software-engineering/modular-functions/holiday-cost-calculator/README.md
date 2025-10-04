# Holiday Cost Calculator

## Overview
A modular Python application demonstrating function decomposition and clean architecture for calculating comprehensive holiday costs.

## 🏗 Architecture Features
- **Function Decomposition**: Complex problem broken into single-responsibility functions
- **Input Validation**: Robust error handling for all user inputs  
- **Separation of Concerns**: Clear distinction between input, calculation, and business logic
- **Modular Design**: Easy to maintain, test, and extend

## 📁 Function Structure

get_city_flight() - User input with validation
get_num_nights() - Input handling with error checking
price_per_night() - Business logic (pricing rules)
hotel_cost() - Calculation module
plane_cost() - Service pricing logic
car_rental() - Customizable options with validation
holiday_cost() - Main orchestrator function
text


## 🚀 Quick Start
```bash
cd programming-software-engineering/modular-functions/holiday-cost-calculator
python holiday_calculator.py

💡 Technical Highlights

    Modular function architecture

    Comprehensive input validation

    Customizable rental options

    Clean separation of concerns

    Production-ready error handling

text


**B. `requirements.txt`:**
```txt
# Built-in Python libraries only
# Demonstrates clean architecture without external dependencies
