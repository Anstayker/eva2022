#import tkinter as tk
#from tkinter import ttk

#from Checkbox import Checkbox


from tkinter import *

# Manipulate data from registration fields
def send_data():
    username_info = username.get()
    password_info = password.get()
    fullname_info = fullname.get()
    age_info = str(age.get())
    print(username_info, "\t", password_info, "\t", fullname_info, "\t", age_info)

    #  Open and write data to a file
    file = open("user.txt", "a")
    file.write(username_info)
    file.write("\t")
    file.write(password_info)
    file.write("\t")
    file.write(fullname_info)
    file.write("\t")
    file.write(age_info)
    file.write("\t\n")
    file.close()
    print(" New user registered. Username: {} | FullName: {}   ".format(username_info, fullname_info))

    #  Delete data from previous event
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    fullname_entry.delete(0, END)
    age_entry.delete(0, END)


# Create new instance - Class Tk()
myWindow = Tk()
myWindow.geometry("650x550")
myWindow.title("Registration Form - Python + Tkinter")
myWindow.resizable(False, False)
myWindow.config(background="#213141")
main_title = Label(text="Python Form | TRUZZ BLOGG", font=("Cambria", 14), bg="#56CD63", fg="black", width="500",
                   height="2")
main_title.pack()

# Define Label Fields
username_label = Label(text="Username", bg="#FFEEDD")
username_label.place(x=22, y=70)
password_label = Label(text="Password", bg="#FFEEDD")
password_label.place(x=22, y=130)
fullname_label = Label(text="Fullname", bg="#FFEEDD")
fullname_label.place(x=22, y=190)
age_label = Label(text="Age", bg="#FFEEDD")
age_label.place(x=22, y=250)

# CheckBox
checkbox = Checkbutton(text="Opcion")
checkbox.place(width=10, height=10)

# Get and store data from users
username = StringVar()
password = StringVar()
fullname = StringVar()
age = StringVar()

username_entry = Entry(textvariable=username, width=40)
password_entry = Entry(textvariable=password, width=40, show="*")
fullname_entry = Entry(textvariable=fullname, width=40)
age_entry = Entry(textvariable=age, width=40)

username_entry.place(x=22, y=100)
password_entry.place(x=22, y=160)
fullname_entry.place(x=22, y=220)
age_entry.place(x=22, y=280)

# Submit Button
submit_btn = Button(myWindow, text="Submit Info", width="30", height="2", command=send_data, bg="#00CD63")
submit_btn.place(x=22, y=320)

myWindow.mainloop()




""""

class Application(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Checkbutton en Tkinter")

        self.checkbox = Checkbox(self,
                                 text="Opcion", command=self.check_clicked)
        self.checkbox.place(x=40, y=70)

        self.place(width=300, height=200)

    def check_clicked(self):
        print(self.checkbox.checked())


main_window = tk.Tk()
app = Application(main_window)
app.mainloop()




------------------------------------------------
"""
""""
window = tk.Tk()
window.title('My Window')
window.geometry('100x100')

l = tk.Label(window, bg='white', width=20, text='empty')
l.pack()


def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love Python ')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='I do not anything')
    else:
        l.config(text='I love both')


var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()

window.mainloop()


------------------------------------------------

"""

