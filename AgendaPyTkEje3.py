#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
from json import loads
from json import dump

def cargar():
    persona = {}

    persona["nombre"] = sd.askstring("consulta", "Ingrese Nombre: ")
    persona["edad"] = sd.askinteger("consulta", "Ingrese Edad: ")
    persona["altura"] = sd.askfloat("consulta", "Ingrese Altura: ")

    with open("persona.json", "w") as archivo:
        dump(persona, archivo)

def mostrar():
    persona = loads(open("persona.json").read())

    mb.showinfo("nombre", persona["nombre"])
    mb.showinfo("edad", persona["edad"])
    mb.showinfo("altura", persona["altura"])

def showFormAddPerson():
    fromAddPerson = tk.Toplevel(mainForm)
    fromAddPerson.geometry("300x800")
    fromAddPerson.title("Agregar Persona...")

    nombreLabel = tk.Label(fromAddPerson, text = "Nombre: ")
    nombreLabel.place(x =20, y =20)
    nombreEntry = tk.Entry(fromAddPerson, width = 30)
    nombreEntry.place(x =20, y =50)

    mostrarButton = tk.Button(fromAddPerson, text = "Mostrar", command = lambda: mostrar_dato(nombreEntry))
    mostrarButton.place(x =20, y =70)

def mostrar_dato(nombreEntry):
    texto = nombreEntry.get()
    mb.showinfo("Dato", texto)

mainForm = tk.Tk()
mainForm.title("Hola TKINTER")
mainForm.geometry("800x400")

mainMenu = tk.Menu(mainForm)

fileMenu = tk.Menu(mainMenu, tearoff = 0)
fileMenu.add_command(label = "Salir", command = quit)
mainMenu.add_cascade(label = "Archivo", menu = fileMenu)

personMenu = tk.Menu(mainMenu, tearoff = 0)
personMenu.add_command(label = "Cargar datos...", command = showFormAddPerson)
personMenu.add_command(label = "Mostrar datos...", command = mostrar)
mainMenu.add_cascade(label = "Personas", menu = personMenu)

mainForm.config(menu = mainMenu)


mainForm.mainloop()
