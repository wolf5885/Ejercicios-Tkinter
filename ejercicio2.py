#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox as mb
from tkinter import simpledialog as sd

def nameAgeHigh():
    resultado = sd.askstring("Nombre", "Ingrese su nombre: ")
    mb.showinfo("resultado", str(resultado))

    resultado = sd.askinteger("Edad", "Ingrese su edad: ")
    mb.showinfo("resultado", str(resultado))

    resultado = sd.askfloat("Altura", "Ingrese su altura: ")
    mb.showinfo("resultado", resultado)

mainForm = tk.Tk()
mainForm.title("Hola TKINTER")
mainForm.geometry("800x400")

boton1 = tk.Button(mainForm, text = "Ingresar N/E/A ", command = nameAgeHigh)
boton1.place(x =50, y =150)

mainForm.mainloop()
