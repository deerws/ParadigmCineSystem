import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import database

class CineSystemApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Paradigm CineSystem')
        self.geometry('750x500')
        self.config(bg='#18161D')
        self.resizable(False, False)

        self.font1 = ('Roboto', 25, 'bold')
        self.font2 = ('Roboto', 13, 'bold')
        self.font3 = ('Roboto', 18, 'bold')

        self.show_initial_screen()

    def show_initial_screen(self):
        self.initial_frame = customtkinter.CTkFrame(self, width=750, height=500, fg_color='#18161D')
        self.initial_frame.pack(fill='both', expand=True)

        self.bg_image = PhotoImage(file="0.png")
        self.bg_label = Label(self.initial_frame, image=self.bg_image, bg = '#000')
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        start_button = customtkinter.CTkButton(self.initial_frame, text="Start", font=self.font3, fg_color='#6ECF00', hover_color='#5CBF00', command=self.show_main_screen)
        start_button.pack(pady=240)

    def show_main_screen(self):
        self.initial_frame.pack_forget()
        self.main_frame = MainFrame(self)
        self.main_frame.pack(fill='both', expand=True)

class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color='#18161D')
        self.master = master
        self.create_widgets()
        self.add_to_treeview()

    def create_widgets(self):
        self.image1 = PhotoImage(file="1.png")
        self.image1_label = Label(self, image=self.image1, bg='#000')
        self.image1_label.place(x=0, y=0)

        self.name_label = customtkinter.CTkLabel(self, font=self.master.font3, text='Username', text_color='#fff', bg_color='#000')
        self.name_label.place(x=130, y=300)

        self.name_entry = customtkinter.CTkEntry(self, font=self.master.font3, text_color='#000', fg_color='#fff', border_color='#18161D', border_width=2, width=160)
        self.name_entry.place(x=290, y=300)

        self.number_label = customtkinter.CTkLabel(self, font=self.master.font3, text='Number of tickets', text_color='#fff', bg_color='#000')
        self.number_label.place(x=130, y=350)

        self.variable1 = StringVar()
        self.options = ['1', '2', '3']

        self.duration_options = customtkinter.CTkComboBox(self, font=self.master.font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#18161D', button_color='#18161D', button_hover_color='#000', border_color='#000', width=160, variable=self.variable1, values=self.options, state='readonly')
        self.duration_options.set('1')
        self.duration_options.place(x=290, y=350)

        self.book_button = customtkinter.CTkButton(self, command=self.book, font=self.master.font3, text_color='#fff', text='Buy Tickets', fg_color='#6ECF00', hover_color='#6D006B', bg_color='#18161D', cursor='hand2', corner_radius=15, width=200)
        self.book_button.place(x=280, y=400)

        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure('Treeview', font=self.master.font2, foreground='#fff', background='#000', fieldbackground='#000')
        self.style.map('Treeview', background=[('selected', '#6ECF00')])

        self.tree = ttk.Treeview(self, height=8)
        self.tree['columns'] = ('Ticket ID', 'Movie Name', 'Available Tickets', 'Ticket Price')
        self.tree.column('#0', width=0, stretch=tk.NO)
        self.tree.column('Ticket ID', anchor=tk.CENTER, width=100)
        self.tree.column('Movie Name', anchor=tk.CENTER, width=100)
        self.tree.column('Available Tickets', anchor=tk.CENTER, width=100)
        self.tree.column('Ticket Price', anchor=tk.CENTER, width=100)
        self.tree.heading('Ticket ID', text='Ticket ID')
        self.tree.heading('Movie Name', text='Movie Name')
        self.tree.heading('Available Tickets', text='Available Tickets')
        self.tree.heading('Ticket Price', text='Ticket Price')
        self.tree.place(x=187, y=80)

    def add_to_treeview(self):
        tickets = database.get_tickets()
        self.tree.delete(*self.tree.get_children())
        for ticket in tickets:
            if ticket[2] > 0:
                self.tree.insert('', END, values=ticket)

    def reservation(self, name, movie, quantity, price):
        customer_name = name
        movie_name = movie
        booked_quantity = quantity
        ticket_price = price
        total_price = ticket_price * booked_quantity

        frame = customtkinter.CTkFrame(self, bg_color='#000', fg_color='#000', corner_radius=10, border_width=2, border_color='#6ECF00', width=200, height=130)
        frame.place(x=500, y=290)

        name_label = customtkinter.CTkLabel(frame, font=self.master.font3, text=f'Username: {customer_name}', text_color='#fff', bg_color='#000')
        name_label.place(x=10, y=10)

        movie_label = customtkinter.CTkLabel(frame, font=self.master.font3, text=f'Movie: {movie_name}', text_color='#fff', bg_color='#000')
        movie_label.place(x=10, y=50)

        total_price_label = customtkinter.CTkLabel(frame, font=self.master.font3, text=f'Total: {total_price}', text_color='#fff', bg_color='#000')
        total_price_label.place(x=10, y=90)

        return total_price

    def book(self):
        customer_name = self.name_entry.get()
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror('Error', 'Choose a ticket to buy.')
        elif not customer_name:
            messagebox.showerror('Error', 'Forgot your username')
        else:
            row = self.tree.item(selected_item)['values']
            movie_name = row[1]
            ticket_price = row[3]
            booked_quantity = int(self.variable1.get())
            if booked_quantity > row[2]:
                messagebox.showerror('Error', 'Not enough tickets.')
            else:
                database.update_quantity(row[0], booked_quantity)
                self.add_to_treeview()
                total_price = self.reservation(customer_name, movie_name, booked_quantity, ticket_price)
                with open('Tickets.txt', 'a') as file:
                    file.write(f'Customer Name: {customer_name}\n')
                    file.write(f'Movie Name: {movie_name}\n')
                    file.write(f'Total Price: {total_price}$\n=================================\n')
                messagebox.showinfo('Success', 'Congratulations, you bought the tickets!')

if __name__ == "__main__":
    app = CineSystemApp()
    app.mainloop()
