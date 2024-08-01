from tkinter import *

def calc():
    miles = float(miles_entry.get())
    km = miles*1.609
    kilometer_label.config(text = f"{km}")

window = Tk()
window.title("Miles to Kilometer Convertor")
window.config(padx=20, pady=20)

miles_entry = Entry(width=7)
miles_entry.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal")
is_equal_label.grid(row=1, column=0)

kilometer_label = Label(text="0")
kilometer_label.grid(row=1, column=1)

k_label = Label(text="Km")
k_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=calc)
calculate_button.grid(row=3, column=1)

window.mainloop()
