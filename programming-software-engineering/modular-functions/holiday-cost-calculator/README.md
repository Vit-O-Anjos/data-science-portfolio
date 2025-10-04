Holiday Cost Calculator

## 🏗 Architecture Showcase
This project demonstrates **modular function design** and **robust input validation** - key skills for production-ready software development.

## 📋 Overview  
This project is a command-line holiday cost calculator that interactively collects user inputs for flight destination, hotel stay, and car rental preferences, validates these inputs with error handling, and computes the total cost of the holiday.

## ⚡ Key Features  
- 🛡️ Robust user input validation using try-except blocks and loops to handle invalid data without crashing  
- ✈️ Selection of flights from predefined cities with corresponding prices  
- 🏨 Hotel stay cost calculation based on city and number of nights  
- 🚗 Optional customized car rental with brand-specific daily rates or default rental cost  
- 🏗️ Modular function design for clarity and reusability  
- 💬 Clear, user-friendly prompts and error messages

## 🚀 Usage
Run the script and answer all prompts. Invalid inputs trigger clear error messages and re-prompts until valid information is provided. The total cost is displayed at the end.

### 💡 Example Interaction:

Enter Lisbon, Porto, Faro, Santa Cruz ou Santa Maria: lisbon
Enter the number of nights: 3
Car rental days: 4
Would you like to customize your rental ride? Y/N: y
Choose between Ferrari, Bugatti, Bentley, Lamborghini, 4L or Cupra: ferrari
The total cost for the holiday is £[calculated_amount].
text


## 📋 Requirements
- Python 3.6 or higher  
- No external libraries required

## 🔧 Notes for Developers
- Global variables are used for shared state and can be refactored for better modularity  
- Input validation follows best practices by continuously prompting until valid input is entered  
- Easily extendable to add more cities, hotels, cars, or pricing rules
