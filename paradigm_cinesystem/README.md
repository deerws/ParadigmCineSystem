# 🎬 Paradigm CineSystem

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/GUI-CustomTkinter-orange.svg" alt="GUI Framework">
  <img src="https://img.shields.io/badge/Database-SQLite-lightgrey.svg" alt="Database">
</div>

## 📖 About the Project

**Paradigm CineSystem** is a modern cinema ticket booking application developed in Python. With an elegant and intuitive graphical interface, the system allows users to view available movies, check prices, and purchase tickets in a simple and efficient way.

### ✨ Key Features

- 🎨 **Modern Interface**: Built with CustomTkinter for an attractive visual experience
- 📊 **Real-time Visualization**: Interactive table showing ticket availability
- 💾 **Data Persistence**: SQLite database for reliable storage
- 🎫 **Receipts**: Automatic generation of purchase receipts
- 🔄 **Automatic Updates**: Instant stock synchronization after purchases

## 🚀 Features

### 🎪 Initial Screen
- Splash screen with custom design
- Initialization button with smooth animations

### 🎯 Booking System
- **Movie Selection**: View all available movies
- **Quantity Control**: Choose from 1 to 3 tickets per purchase
- **Smart Validation**: Automatic availability verification
- **Purchase Confirmation**: Visual transaction feedback

### 📋 Data Management
- **Database**: SQLite with optimized ticket table
- **Log Files**: Complete history of all transactions
- **Input Validation**: Protection against invalid data

## 🛠️ Technologies Used

| Technology | Version | Purpose |
|-----------|--------|-----------|
| **Python** | 3.7+ | Main language |
| **CustomTkinter** | Latest | Modern GUI framework |
| **Tkinter** | Built-in | Complementary widgets |
| **SQLite3** | Built-in | Database |

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### 🔧 Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/deerws/oop_pratices/paradigm_cinesystem.git
   cd paradigm_cinesystem
   ```

2. **Install dependencies**
   ```bash
   pip install customtkinter
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

## 🗂️ Project Structure

```
ParadigmCineSystem/
├── 📁 assets/
│   ├── 0.png              # Initial screen image
│   └── 1.png              # Main screen image
├── 📄 database.py         # Database operations
├── 📄 main.py            # Main application logic
├── 📄 Reservation.db     # SQLite database (auto-generated)
├── 📄 Tickets.txt        # Receipt file (auto-generated)
└── 📄 README.md          # Project documentation
```

## 🎯 How to Use

### 1️⃣ Starting the Application
- Run the `main.py` file
- Click the **"Start"** button on the initial screen

### 2️⃣ Buying Tickets
1. **Select a movie** from the available movies table
2. **Enter your name** in the "Username" field
3. **Choose the quantity** of tickets (1-3)
4. **Click "Buy Tickets"** to confirm

### 3️⃣ Confirmation
- ✅ Success message will be displayed
- 📋 Receipt will be saved in `Tickets.txt`
- 🔄 Stock will be updated automatically

## 🗄️ Database Structure

### Table: `Tickets`
| Field | Type | Description |
|-------|------|-----------|
| `ticket_id` | INTEGER | Unique ticket identifier |
| `movie_name` | TEXT | Movie name |
| `ticket_quantity` | INTEGER | Available quantity |
| `ticket_price` | REAL | Price per ticket |

## 📱 User Interface

### Main Components
- **Treeview**: Tabular display of movies
- **Entry Field**: Input field for username
- **ComboBox**: Ticket quantity selection
- **Buttons**: System interaction
- **Labels**: Information and feedback

### Color Scheme
- **Background**: `#18161D` (Dark gray)
- **Highlight**: `#6ECF00` (Vibrant green)
- **Text**: `#FFFFFF` (White)
- **Components**: `#000000` (Black)

## 🔧 Customization

### Modifying Movies
Edit the `database.py` file to add/remove movies:

```python
# Example insertion
cursor.execute("INSERT INTO Tickets VALUES (?, ?, ?, ?)", 
               (4, "New Movie", 10, 25.00))
```

### Changing Limits
Modify the `self.options` list in `main.py` to change the maximum number of tickets:

```python
self.options = ['1', '2', '3', '4', '5']  # Allows up to 5 tickets
```

## 🤝 Contributing

Contributions are welcome! To contribute:

1. 🍴 Fork the project
2. 🌟 Create a branch for your feature (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔍 Open a Pull Request

## 🐛 Known Issues

- Images must be in the root directory
- Maximum quantity limited to 3 tickets
- Basic input validation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@deerws](https://github.com/deerws)
- Email: paes.andre33@gmail.com

---

<div align="center">
  <p>⭐ If this project was useful to you, consider giving it a star!</p>
  <p>🎬 Made with ❤️ for cinema enthusiasts</p>
</div>
