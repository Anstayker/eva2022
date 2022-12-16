# import tkinter as tk
# from tkinter import ttk

# from Checkbox import Checkbox


from tkinter import *
import json


# Manipulate data from registration fields
def send_data():
    pregunta_info = pregunta.get()
    opcionA_info = opcionA.get()
    opcionB_info = opcionB.get()
    opcionC_info = opcionC.get()

    resCorrecta = optionMenuVar.get()
    if(resCorrecta=="Opción A"):
        resCorrecta = opcionA_info
    if(resCorrecta == "Opción B"):
        resCorrecta = opcionB_info
    if(resCorrecta=="Opción C"):
        resCorrecta = opcionC_info

    currentId = 1;

    #  Open and write data to a file
    aList = [
        {
            'id': currentId,
            'question': pregunta_info,
            'options': [
                {"a": opcionA_info,
                 "b": opcionB_info,
                 "c": opcionC_info}
            ],
            "answer": resCorrecta,
            "score": 0,
            "status": ""
        },
        {
            'id': currentId + 1,
            'question': pregunta_info,
            'options': [
                {"a": opcionA_info,
                 "b": opcionB_info,
                 "c": opcionC_info}
            ],
            "answer": resCorrecta,
            "score": 0,
            "status": ""
        }
    ]
    jsonString = json.dumps(aList)
    jsonFile = open("quiz.json", 'w')
    jsonFile.write(jsonString)
    jsonFile.close()
    print(jsonString)


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
pregunta_label = Label(text="Ingrese la pregunta", bg="#FFEEDD")
pregunta_label.place(x=22, y=70)
opcionA_label = Label(text="Opción A", bg="#FFEEDD")
opcionA_label.place(x=22, y=130)
opcionB_label = Label(text="Opción B", bg="#FFEEDD")
opcionB_label.place(x=22, y=190)
opcionC_label = Label(text="Opción C", bg="#FFEEDD")
opcionC_label.place(x=22, y=250)

# Get and store data from users
pregunta = StringVar()
opcionA = StringVar()
opcionB = StringVar()
opcionC = StringVar()

pregunta_entry = Entry(textvariable=pregunta, width=40)
opcionA_entry = Entry(textvariable=opcionA, width=40)
opcionB_entry = Entry(textvariable=opcionB, width=40)
opcionC_entry = Entry(textvariable=opcionC, width=40)

pregunta_entry.place(x=22, y=100)
opcionA_entry.place(x=22, y=160)
opcionB_entry.place(x=22, y=220)
opcionC_entry.place(x=22, y=280)

# Drop Down

options = [
    "Opción A",
    "Opción B",
    "Opción C"
]

optionMenuVar = StringVar()
optionMenuVar.set(options[0])

optionSelected = StringVar()
optionSelected.set(options[0])

dropDown_label = Label(text="Seleccione la respuesta", bg="#FFEEDD")
dropDown_label.place(x=22, y=310)

drop = OptionMenu(myWindow, optionSelected, *options)
drop.place(x=22, y=340)

#w = OptionMenu(optionMenuVar, *options)
#w.pack()

# Submit Button
submit_btn = Button(myWindow, text="Subir pregunta", width="30", height="2", command=send_data, bg="#00CD63")
submit_btn.place(x=22, y=400)

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
