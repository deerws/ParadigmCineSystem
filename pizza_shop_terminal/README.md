# Vesuvio's Pizza - Order System

A terminal-based pizza ordering system where customers and employees can register, authenticate, and interact with the menu. The system allows customers to place orders and employees to check work shifts.

## 🍕 Features

- Registration and authentication for customers and employees
- Display of available pizza menu
- Order placement
- Employee work shift display

## 🏗️ Code Structure

The system consists of four main classes:

- **Username**: Base class that stores name and password
- **Cliente**: Inherits from Username, allowing customer registration and authentication
- **Funcionario**: Inherits from Username, allowing employee registration and authentication
- **Pizza**: Defines pizza flavors and prices
- **Service**: Manages menu display and order processing

## 🚀 How to Run

### Prerequisites
- Python 3.x installed on your system

### Installation and Execution Steps

1. Make sure you have Python installed

2. Clone this repository:
```bash
git clone https://github.com/deerws/vesuvios-pizza.git
```

3. Navigate to the project directory:
```bash
cd vesuvios-pizza
```

4. Run the main script:
```bash
python vesuvios_pizza.py
```

5. Follow the instructions displayed on the terminal

## 🔮 Future Improvements

- Implement a database to store customer and order information
- Develop a graphical user interface for better user experience
- Add pizza customization options

## 🙌 Credits

Developed by **André Pinheiro Paes** - CS Student (UFSC).

---

Enjoy your pizza! 🍕
