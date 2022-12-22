# import tkinter as tk
# from tkinter import ttk
import tkinter
# from Checkbox import Checkbox


from tkinter import *
import json
import os
from zipfile import ZipFile

currentId = 1


def get_all_file_paths(directory):
    # initializing empy file paths list
    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    # returning all file paths
    return file_paths


def make_json():
    # path to folder which needs to be zipped
    directory = './'

    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(directory)

    # printing the list of all files to be zipped
    print('Following files will be zipped in this program: ')
    for file_name in file_paths:
        print(file_name)

    # writing files to a zipfile
    with ZipFile('Scorm_Package.zip', 'w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)

    print('All files zipped successfully')


def send_data():
    global currentId

    pregunta_info = pregunta.get()
    opcionA_info = opcionA.get()
    opcionB_info = opcionB.get()
    opcionC_info = opcionC.get()
    puntaje_info = score_entry.get()

    resCorrecta = optionSelected.get()
    print(resCorrecta)
    if (resCorrecta == "Opción A"):
        resCorrecta = opcionA_info
    if (resCorrecta == "Opción B"):
        resCorrecta = opcionB_info
    if (resCorrecta == "Opción C"):
        resCorrecta = opcionC_info

    #  Open and write data to a file
    aList = {
        'id': currentId,
        'question': pregunta_info,
        'options': [
            {"a": opcionA_info,
             "b": opcionB_info,
             "c": opcionC_info}
        ],
        "answer": resCorrecta,
        "score": 0,
        "status": "",
        "puntaje": puntaje_info
    }

    currentId += 1

    listOfQuestions.append(aList)

    jsonString = json.dumps(listOfQuestions)
    jsonFile = open("quiz.json", 'w')
    jsonFile.write(jsonString)
    jsonFile.close()
    dropDown_label.place(x=22, y=310)

    navigation_label = Label(text=str(currentId) + "/" + str(currentId))
    navigation_label.place(x=125, y=458)

    pregunta_entry.delete(0, tkinter.END)
    opcionA_entry.delete(0, tkinter.END)
    opcionB_entry.delete(0, tkinter.END)
    opcionC_entry.delete(0, tkinter.END)

    print(jsonString)


# Create new instance - Class Tk()
myWindow = Tk()
myWindow.geometry("280x650")
myWindow.title("Cuestionario")
myWindow.resizable(False, False)
myWindow.config(background="#213141")
main_title = Label(text="Authoring tool - Cuestionario", font=("Cambria", 14), bg="#56CD63", fg="black", width="500",
                   height="2")
main_title.pack()

# Variables

listOfQ = []
listOfQuestions = []

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


# Score Label

score_label = Label(text="Asigne un puntaje", bg="#FFEEDD")
score_label.place(x=22, y=390)

score = IntVar()
score_entry = Entry(textvariable=score, width=10)
score_entry.place(x=50, y=420)


# Action Buttons
back_btn = Button(myWindow, text="<-", width=5, height=1, bg="#00CD63")
back_btn.place(x=22, y=455)

navigation_label = Label(text=str(currentId) + "/" + str(currentId))
navigation_label.place(x=125, y=458)

back_btn = Button(myWindow, text="->", width=5, height=1, bg="#00CD63")
back_btn.place(x=197, y=455)

# Submit Button
submit_btn = Button(myWindow, text="Subir pregunta", width="30", height="2", command=send_data, bg="#00CD63")
submit_btn.place(x=22, y=485)

# Make Json Button
submit_btn = Button(myWindow, text="Empaquetar", width="30", height="2", command=make_json, bg="#00CD63")
submit_btn.place(x=22, y=530)

myWindow.mainloop()


def modifyList():
    pregunta_info = pregunta.get()
    opcionA_info = opcionA.get()
    opcionB_info = opcionB.get()
    opcionC_info = opcionC.get()

    listOfQ.append()
