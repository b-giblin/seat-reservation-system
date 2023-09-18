import tkinter as tk
from tkinter import messagebox
import numpy as np

# Initialize a new seat object
class Seat:
  def __init__(self, row, column): #Args
    self.row = row  # row: The row number of the seat 
    self.column = column  # column: The column number of the seat
    self.is_reserved = False

# Reserves the seat and returns True if the seat was successfully reserved and False otherwise.
  def reserve(self):
    if not self.is_reserved:
      self.is_reserved = True
      return True
    return False
  

# Creates a class that represents the cinema hall.
class CinemaHall:  # Initializes a new cinema hall object
  def __init__(self, rows, columns): # Args 
    self.rows = rows  # rows: The number of rows in the cinema hall
    self.columns = columns  # columns: The number of columns in the cinema hall
    self.matrix = np.array([[Seat(row, col) for col in range(columns)] for row in range(rows)]) # list comprehension to populate the matrix


# Reserves a seat in the cinema hall
  def reserve_seat(self, row, column):  # Args- row: the row number of the seat to reserve | column: The column number of the seat to reserve
    if 0 <= row < self.rows and 0 <= column < self.columns: 
      return self.matrix[row, column].reserve()  # Returns true if seat was successfully reserved, False otherwise
    return False
  

# Counts the number of available seats in the cinema hall  
  def available_seats(self):
    count = sum(1 for row in self.matrix for seat in row if not seat.is_reserved)
    return count  # Returns the number of available seats in the cinema hall


# Initialize a new cinema app object 
class CinemaApp(tk.Tk):
  def __init__(self, cinema, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.cinema = cinema
    self.title("Cinema Hall Reservation System")
    self.geometry("300x300")
    self.setup_ui()


# Creates the GUI for the application.
  def setup_ui(self):
    for r in range(self.cinema.rows):
      for c in range(self.cinema.columns):
        btn = tk.Button(self, text="0", width=5, height=2, command=lambda r=r, c=c: self.reserve_seat(r, c))
        btn.grid(row=r, column=c, padx=5, pady=5)
    self.update_seating()


# Reserves a seat in the cinema hall 
  def reserve_seat(self, row, col):  # Args- row: the row number of the seat to reserve | col: the column number of the seat to reserve
    if self.cinema.reserve_seat(row, col):
      messagebox.showinfo("Success", "Seat successfully reserved!")
      self.update_seating()
    else:
      messagebox.showerror("Error", "Seat is already reserved")


# Updates the GUI to reflect the current seating arrangement. 
  def update_seating(self):
    for r, row in enumerate(self.cinema.matrix):
      for c, seat in enumerate(row):
        btn = self.grid_slaves(row=r, column=c)[0]
        if seat.is_reserved:
          btn.config(text="X", state=tk.DISABLED)
        else:
          btn.config(text="0", state=tk.NORMAL)

if __name__ == "__main__":
  cinema = CinemaHall(5,5)
  app = CinemaApp(cinema)
  app.mainloop()  # Start Mainloop of the application