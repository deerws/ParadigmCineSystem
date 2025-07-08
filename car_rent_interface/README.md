# 🚗 Car Rental Application

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/GUI-CustomTkinter-orange.svg" alt="GUI Framework">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen.svg" alt="Status">
</div>

## 📖 About the Project

The **Car Rental Application** is a modern desktop application built with Python and CustomTkinter that provides an intuitive interface for car rental services. The application features a sleek dark theme design with smooth user interactions, making it easy for customers to browse available vehicles, calculate rental costs, and complete their booking process.


## 🛠️ Technical Specifications

### Technologies Used
| Technology | Version | Purpose |
|-----------|---------|---------|
| **Python** | 3.7+ | Core programming language |
| **CustomTkinter** | Latest | Modern GUI framework |
| **Tkinter** | Built-in | Image handling and base widgets |

### Application Architecture
- **Object-Oriented Design**: Clean class-based structure
- **Event-Driven Programming**: Responsive user interactions
- **Modular Layout**: Separate methods for different screens
- **State Management**: Dynamic screen transitions

## 📦 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager
- Operating System: Windows, macOS, or Linux

### 🔧 Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/deerws/opp_pratices/car_rental_interface.git
   cd car_rental_interface
   ```

2. **Install dependencies**
   ```bash
   pip install customtkinter
   ```

3. **Add required assets**
   - Ensure `image.png` is in the root directory
   - The image serves as the background for the login screen

4. **Run the application**
   ```bash
   python main.py
   ```

## 🗂️ Project Structure

```
car-rental-interface/
├── 📄 main.py              # Main application file
├── 🖼️ image.png            # Background image asset
├── 📄 README.md            # Project documentation
└── 📄 LICENSE
```

## 🎯 Usage Guide

### 1️⃣ Starting the Application
- Launch the application using `python main.py`
- The login screen will appear with the welcome message

### 2️⃣ User Authentication
- Enter your **username** in the first field
- Enter your **password** (masked with asterisks)
- Check **"Remember me"** if desired
- Click **"LOGIN"** to proceed

### 3️⃣ Car Rental Process
- **Model Selection**: Enter the desired car model
- **Price Entry**: Input the daily rental rate
- **Duration**: Specify number of rental days
- **Confirmation**: Click **"JOIN THE RIDE"** to complete

### 4️⃣ Results
- View rental details in the console output
- Total cost calculated automatically
- Confirmation message displayed

## 💻 Code Structure

### Main Components

#### `App` Class
The main application class that handles:
- Window configuration and styling
- Screen transitions
- User input processing
- Cost calculations

#### Key Methods

| Method | Purpose |
|--------|---------|
| `configuracao_da_janela_inicial()` | Sets up main window properties |
| `background()` | Configures theme and appearance |
| `login_screen()` | Creates authentication interface |
| `forms()` | Displays rental selection form |
| `open()` | Processes booking and calculates costs |

### UI Components

#### Login Screen Elements
- **CTkLabel**: Welcome message and form titles
- **CTkEntry**: Username and password input fields
- **CTkCheckBox**: "Remember me" option
- **CTkButton**: Login action button

#### Rental Form Elements
- **CTkEntry**: Model, price, and duration inputs
- **CTkButton**: Booking confirmation button
- **CTkTextbox**: Vehicle information display

## 🎨 Design Features

### Visual Elements
- **Color Scheme**: Dark theme with purple accents
- **Typography**: Century Gothic font family
- **Layout**: Grid-based positioning system
- **Responsiveness**: Fixed 1000x400 pixel window

### User Experience
- **Intuitive Navigation**: Clear step-by-step process
- **Visual Feedback**: Button hover effects and styling
- **Error Prevention**: Input validation and type checking
- **Professional Appearance**: Modern CustomTkinter styling


## 🐛 Known Issues

- Application requires `image.png` in the root directory
- Console output only (no GUI-based results display)
- No data persistence between sessions
- Limited input validation

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. 🍴 Fork the repository
2. 🌟 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔍 Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@deerws](https://github.com/deerws)
- Email: paes.andre33@gmail.com

---

<div align="center">
  <p>⭐ If this project was helpful, please give it a star!</p>
  <p>🚗 Made with ❤️ for car rental enthusiasts</p>
</div>
