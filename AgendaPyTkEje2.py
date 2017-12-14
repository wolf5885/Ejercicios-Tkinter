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


mainForm = tk.Tk()
mainForm.title("Hola TKINTER")
mainForm.geometry("800x400")

mainMenu = tk.Menu(mainForm)

fileMenu = tk.Menu(mainMenu, tearoff = 0)
fileMenu.add_command(label = "Salir", command = quit)
mainMenu.add_cascade(label = "Archivo", menu = fileMenu)

personMenu = tk.Menu(mainMenu, tearoff = 0)
personMenu.add_command(label = "Cargar datos...", command = cargar)
personMenu.add_command(label = "Mostrar datos...", command = mostrar)
mainMenu.add_cascade(label = "Personas", menu = personMenu)

mainForm.config(menu = mainMenu)


mainForm.mainloop()
