#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox as mb

def saludar():
    resultado = mb.askyesnocancel("Consulta", "Te gusta python?: ")
    mb.showinfo("resultado", str(resultado))

    resultado = mb.askyesno("Pregunta", "Te gusta python?: ")
    mb.showinfo("resultado", str(resultado))

    resultado = mb.askretrycancel("Pregunta", "Te gusta python?: ")
    mb.showwarning("resultado", str(resultado))

    resultado = mb.askokcancel("Saludar", "Hola: ")
    mb.showerror("resultado", str(resultado))

    
    

mainForm = tk.Tk()
mainForm.title("Hola TKINTER")
mainForm.geometry("800x400")

botonSaludar = tk.Button(mainForm, text = "Saludar", command = saludar)
botonSaludar.place(x = 20, y = 20)

mainForm.mainloop()


