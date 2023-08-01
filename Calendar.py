from tkinter import *
from tkcalendar import *

root = Tk()
root.title("Calendar")
root.geometry("600x600")

def date_show():
    my_label.config(text=f"Today's Date Is: {cal.get_date()}", fg="blue",)


cal = Calendar(root, selectmode="day", )
cal.pack(pady=20, fill="both", expand=True)

my_label = Label(root, text="", font=("Arial", 20), fg="white")
my_label.pack(pady=10)

my_button = Button(root, text='Select Date', command=date_show,)
my_button.pack(pady=20)

root.mainloop()
