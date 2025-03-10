# Paradigm CineSystem

## Description
Paradigm CineSystem is a movie ticket booking application built with Python using Tkinter and CustomTkinter for the GUI. It integrates with an SQLite database to manage movie tickets, allowing users to view available tickets and purchase them.

## Features
- Interactive GUI using CustomTkinter
- View available movie tickets in a table
- Purchase tickets with real-time database updates
- Store ticket reservations in a text file
- Persistent storage using SQLite

## Technologies Used
- Python
- Tkinter & CustomTkinter
- SQLite3

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/deerws/ParadigmCineSystem.git
   cd ParadigmCineSystem
   ```
2. Install dependencies:
   ```bash
   pip install customtkinter
   ```
3. Run the application:
   ```bash
   python main.py

## Database Setup
The application automatically creates and populates an SQLite database (`Reservation.db`) on the first run. The table `Tickets` contains the following columns:
- `ticket_id`: Unique identifier for each ticket
- `movie_name`: Name of the movie
- `ticket_quantity`: Number of tickets available
- `ticket_price`: Price per ticket

## Usage
1. Launch the application.
2. Click "Start" to enter the main screen.
3. Select a movie ticket from the list.
4. Enter your username and choose the number of tickets.
5. Click "Buy Tickets" to confirm the purchase.
6. A reservation receipt will be saved in `Tickets.txt`.

## File Structure
```
ParadigmCineSystem/
│── database.py         # Database handling (SQLite operations)
│── main.py            # Main application logic (GUI & event handling)
│── Reservation.db     # SQLite database file (auto-generated)
│── 0.png, 1.png       # UI assets (background images)
│── Tickets.txt        # Stores ticket purchase records
│── README.md          # Project documentation
```

## Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to submit a pull request.


