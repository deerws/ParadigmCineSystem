import sqlite3

def create_table():
    conn = sqlite3.connect('Reservation.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Tickets (
            ticket_id TEXT PRIMARY KEY,
            movie_name TEXT,
            ticket_quantity INTEGER,
            ticket_price INTEGER)''')
    conn.commit()
    conn.close()

def insert_Tickets():
    conn = sqlite3.connect('Reservation.db')
    cursor = conn.cursor()
    Tickets_data = [
        ('T1', 'Shrek 2', 3, 10),
        ('T2', 'Miranha', 2, 15),
        ('T3', 'Frozen', 4, 13),
        ('T4', 'Bee Movie', 5, 10),
        ('T5', 'Emoji Movie', 1, 25)
    ]
    cursor.executemany('INSERT OR IGNORE INTO Tickets (ticket_id, movie_name, ticket_quantity, ticket_price) VALUES (?,?,?,?)', Tickets_data)
    conn.commit()
    conn.close()

def get_tickets():
    conn = sqlite3.connect('Reservation.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Tickets')
    tickets = cursor.fetchall()
    conn.close()
    return tickets

def update_quantity(id, reserved_quantity):
    conn = sqlite3.connect('Reservation.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE Tickets SET ticket_quantity = ticket_quantity - ? WHERE ticket_id = ?', (reserved_quantity, id))
    conn.commit()
    conn.close()

create_table()
insert_Tickets()
