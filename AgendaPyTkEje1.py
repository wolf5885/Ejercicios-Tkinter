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

botonCargar = tk.Button(mainForm, text = "Cargar", command = cargar)
botonCargar.place(x =20, y =20)

botonMostrar = tk.Button(mainForm, text = "Mostrar", command = mostrar)
botonMostrar.place(x =20, y =60)

mainForm.mainloop()
