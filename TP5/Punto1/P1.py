from io import open
import tkinter as tk
from tkinter import simpledialog, messagebox
import re


def pedir_entrada(prompt):
    # Crear la ventana principal (oculta)
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    # Mostrar el cuadro de diálogo de entrada
    entrada = simpledialog.askstring(title="Entrada", prompt=prompt)

    # Cerrar la ventana principal
    root.destroy()

    return entrada


def mostrar_error(mensaje):
    # Crear la ventana principal (oculta)
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    # Mostrar el mensaje de error
    messagebox.showerror("Error", mensaje)

    # Cerrar la ventana principal
    root.destroy()


def mostrar_info(mensaje):
    # Crear la ventana principal (oculta)
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    # Mostrar el mensaje de información
    messagebox.showinfo("Información", mensaje)

    # Cerrar la ventana principal
    root.destroy()

# 33


def leerLista():
    lista_txt = open('../TP5/alumnos.txt', 'r')
    lista_alumnos = []
    for alumno_txt in lista_txt:
        datos = alumno_txt.strip().split(",")

        alumno = {
            "DNI": datos[0].strip(),
            "Nombre": datos[1].strip(),
            "Nota": datos[2].strip()
        }
        lista_alumnos.append(alumno)

    return lista_alumnos


def mostrar_lista(lista):
    mostrar = "LISTA DE ALUMNOS: \n-------------"
    for alumno in lista:
        mostrar += f"""
DNI: {alumno["DNI"]}
Nombre: {alumno["Nombre"]}
Nota: {alumno["Nota"]}
-----------------------"""
    mostrar_info(mostrar)


def validarDniABuscar():
    while True:
        dni = pedir_entrada("Ingrese el DNI: ")

        if len(dni) == 8 and dni.isdigit():
            break
        else:
            mostrar_error(
                "El DNI debe tener hasta 8 dígitos y solo contener números.")
    return dni


def validarNota():
    while True:
        try:
            nota = int(pedir_entrada("Ingrese la nueva nota: "))
            if 0 <= nota <= 10:
                break
            else:
                mostrar_error("La nota debe estar entre 0 y 10")
        except ValueError:
            mostrar_error("Ingrese un valor correcto")
    return nota


def modificarNotaAlumno(lista):
    dni_a_buscar = validarDniABuscar()
    encontrado = False
    index = 0
    for i in range(len(lista)):
        if lista[i]["DNI"] == dni_a_buscar:
            encontrado = True
            nuevaNota = validarNota()
            lista[index]["Nota"] = nuevaNota
            mostrar_info("Nota modificada!")

    if not encontrado:
        mostrar_error("No se encontró el alumno con tal DNI")


def main():
    lista_alumnos = leerLista()
    while True:
        try:
            op = int(pedir_entrada(f"""Ingresa una opción:
        1-Mostrar lista de alumnos
        2-Modificar nota de alumno
        3-Salir
                                 """))
        except ValueError:
            mostrar_info("Ingrese solo un número")

        if op:
            if op == 1:
                mostrar_lista(lista_alumnos)
            elif op == 2:
                modificarNotaAlumno(lista_alumnos)

            elif op == 3:
                mostrar_info("Saliendo...")
                break


main()
