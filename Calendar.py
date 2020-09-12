from tkinter import *
from tkcalendar import *

root = Tk()
root.title("Calendar")
root.geometry('700x300')

calendar = Calendar(root, selectmode="day", year=2020, month=9, day=12)
calendar.pack(pady=10,fill="both",expand=True)

root.mainloop()


