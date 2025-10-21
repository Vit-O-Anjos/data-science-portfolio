# 🧳 Holiday Cost Calculator

**Skills:** Python · Error Handling · Input Validation · Functional Programming · CLI Development · Software Architecture

## 📖 Overview
A Python-based holiday planning tool that demonstrates **production-ready software engineering practices**. Built as a practical exercise in software engineering fundamentals, it showcases skills directly applicable to production software development through robust input validation and modular architecture.

## 🏗 Architecture Showcase
This project exemplifies **professional software development** through:
- **Modular Function Design** - Clean separation of concerns for maintainability
- **Robust Error Handling** - Comprehensive input validation using try-except blocks
- **User Experience Focus** - Intuitive prompts with guided decision flow  
- **Production-Ready Code** - Scalable structure suitable for real-world applications

## ⚡ Key Features
- ✈️ **Smart Flight Selection** - Choose from predefined cities with validated pricing
- 🏨 **Flexible Hotel Stays** - Dynamic cost calculation based on location and duration
- 🚗 **Custom Car Rentals** - Optional premium vehicle selection with brand-specific pricing
- 🛡️ **Bulletproof Validation** - Continuous prompts until valid input with clear error messages
- 💰 **Real-time Cost Calculation** - Instant total cost updates across all service categories

## 🛠 Technologies & Concepts
- **🐍 Python 3.6+** - Core programming language (no external dependencies)
- **🔄 Functional Programming** - Modular, reusable functions for each calculation component
- **🛡 Defensive Programming** - Comprehensive input validation and error handling
- **📐 Clean Code Principles** - Readable, maintainable, and extensible codebase
- **👥 User-Centered Design** - Intuitive console interface with guided workflows

## 🎯 Engineering Skills Demonstrated
- **📋 Modular Architecture** - Designed maintainable functions for real-world scalability
- **🛡 Production Validation** - Implemented robust input handling using exception management
- **✨ Clean Code Implementation** - Applied software engineering best practices throughout
- **🔧 Extensible Design** - Built foundation for easy feature additions and modifications
- **💡 Problem Solving** - Transformed complex requirements into elegant, working solutions

## 🚀 Quick Start

### Installation & Usage

python holiday_cost_calculator.py

text

💡 Example Interaction

Enter destination (Lisbon, Porto, Faro, Santa Cruz, Santa Maria): lisbon
Enter the number of nights at hotel: 3
Enter car rental days: 4
Customize your rental ride? (Y/N): y
Choose car brand (Ferrari, Bugatti, Bentley, Lamborghini, 4L, Cupra): ferrari

🧾 HOLIDAY COST BREAKDOWN:
✈️ Flight to Lisbon: £590
🏨 3 nights hotel: £1890
🚗 4 days Ferrari rental: £6800
💷 TOTAL HOLIDAY COST: £9280

text

## 📊 Pricing Structure
**Flights:**  
Lisbon: £590 | Porto: £430 | Faro: £650 | Santa Cruz: £780 | Santa Maria: £980

**Hotels (per night):**  
Lisbon: £630 | Porto: £540 | Faro: £520 | Santa Cruz: £490 | Santa Maria: £460

**Car Rentals (per day):**  
Default: £90 | Ferrari: £1700 | Bugatti: £2400 | Bentley: £1200 | Lamborghini: £1550 | 4L: £10 | Cupra: £150

## 💼 Real-World Applications
The patterns demonstrated in this project scale to enterprise development:  
- Input validation → API request handling, form processing, data sanitization  
- Modular functions → Microservices architecture, testable code, team collaboration  
- Error handling → Production system resilience, graceful failure recovery  
- User flow design → Customer-facing applications, onboarding experiences

## 🔧 Development Notes
**Current Architecture & Design Decisions:**  
- Global State Management: Using `city_flight`, `custom_rental`, `chosen_rental` variables for shared state; future versions can migrate toward full parameterization  
- Input Validation: Robust validation using loops and try-except blocks provides full crash protection  
- Business Logic Abstraction: Core logic abstracted into reusable functions for easy updates  
- Testability & Scalability: Modular structure supports testing and future enhancements  

**Technical Trade-offs:**  
- Uses simple global state for MVP simplicity while maintaining clear upgrade paths  
- Balance struck between user-friendly prompts and code complexity  
- Designed for easy extension without major refactoring  

## 📈 Future Enhancements
- Immediate: Additional destination cities and hotel options  
- Medium-term: Seasonal pricing algorithms, package deals, currency conversion  
- Long-term: GUI interface, comprehensive test suite, API integration  
- Architectural: Migration to class-based design to eliminate global state  

## 📋 Requirements
- Python 3.6 or higher  
- No external libraries required  

*Built with ❤️ to showcase professional Python development skills and software engineering principles*
