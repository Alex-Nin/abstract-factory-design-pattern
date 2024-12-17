# Driver System with Abstract Factory

This Python project demonstrates the Abstract Factory design pattern through a driver management system that allows switching between high-resolution and low-resolution drivers for display and printing. The abstract factory encapsulates driver creation, providing a consistent interface for initializing and using different driver configurations.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Project Overview](#project-overview)
4. [Key Features](#key-features)
5. [Purpose and Lessons Learned](#purpose-and-lessons-learned)

## Installation

To set up and run this project locally:

1. **Clone the Repository:**  
```bash
git clone https://github.com/alex-nin/abstract-factory-design-pattern.git
cd abstract-factory-design-pattern
```

2. **Install Dependencies:** Ensure you have Python 3.x installed.

## Usage

To run the program, execute the following command in your terminal in the program directory, depending on your Python environment:

```bash
python abstract_factory.py
```
or
```bash
python3 abstract_factory.py
```

## Project Overview

The main components of this system include:
- **Driver Classes**: The system contains four singleton driver classes for display and print operations:
  - `LowResDisplayDriver` and `HighResDisplayDriver`: Manage display output for low and high resolution.
  - `LowResPrintDriver` and `HighResPrintDriver`: Handle printing operations for low and high resolution.
- **DriverFactory Interface**: An abstract base class defining methods to create display and print drivers.
- **Concrete Factories**: `LowResFactory` and `HighResFactory` implement `DriverFactory` to create low-resolution and high-resolution drivers, respectively. These factories encapsulate driver instantiation and ensure consistent usage across different parts of the system.

## Key Features

1. **Resolution-Specific Drivers**: The system supports both low and high-resolution drivers for display and print, providing tailored driver instances as needed.
2. **Singleton Implementation**: Each driver class is implemented as a singleton, ensuring only one instance exists for each driver type.
3. **Abstract Factory Pattern**: By using the Abstract Factory pattern, the system can easily switch between different driver configurations without modifying client code.
4. **Extensibility**: New driver types or resolutions can be added by creating additional factory and driver classes, enabling scalability.

## Purpose and Lessons Learned

This project helped me understand the Abstract Factory design pattern, particularly how it provides a way to encapsulate a family of related classes. By implementing resolution-specific drivers as singletons and using factories to manage them, I saw how Abstract Factory simplifies the process of creating and using objects that belong together logically. This approach reinforced the value of the Abstract Factory pattern in creating flexible, easily extensible systems.

