import tkinter as tk
from tkinter import messagebox
import numpy as np

class Seat:
  def __init__(self, row, column):
    self.row = row
    self.column = column
    self.is_reserved = False


  def reserve(self):
    if not self.is_reserved:
      self.is_reserved = True
      return True
    return False
  

class CinemaHall:
  def __init__(self, rows, columns):
    self.rows = rows
    self.columns = columns
    self.matrix = np.array([[Seat(row, col) for col in range(columns)] for row in range(rows)])


  def reserve_seat(self, row, column):
    if 0 <= row < self.rows and 0 <= column < self.columns:
      return self.matrix[row, column].reserve()
    return False
  
  def available_seats(self):
    count = sum(1 for row in self.matrix for seat in row if not seat.is_reserved)
    return count
  
class CinemaApp(tk.Tk):
  def __init__(self, cinema, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.cinema = cinema
    self.title("Cinema Hall Reservation System")
    self.geometry("300x300")
    self.setup_ui()


  def setup_ui(self):
    for r in range(self.cinema.rows):
      for c in range(self.cinema.columns):
        btn = tk.Button(self, text="0", width=5, height=2, command=lambda r=r, c=c: self.reserve_seat(r, c))
        btn.grid(row=r, column=c, padx=5, pady=5)
    self.update_seating()

  def reserve_seat(self, row, col):
    if self.cinema.reserve_seat(row, col):
      messagebox.showinfo("Success", "Seat successfully reserved!")
      self.update_seating()
    else:
      messagebox.showerror("Error", "Seat is already reserved")

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
  app.mainloop()