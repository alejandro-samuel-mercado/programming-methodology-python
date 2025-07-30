from io import open
import os

# CREAR O SOBREESCRIBIR UN ARCHIVO
texto = "Nombre: Nunu \nApellido: Cars"
try:
    with open('./text.txt', 'w') as fichero:
        fichero.write(texto)
        fichero.close()
except Exception as e:
    print(f"Error: {e}")

# LEER FICHERO
try:
    with open('text.txt', 'r') as fichero:
        text = fichero.read()
        fichero.close()
        print(text)
except Exception as e:
    print(f"Error: {e}")


# LEER Y ESCRIBIR
try:
    with open('text.txt', 'r+') as fichero:
        text = fichero.read()
        print(text)

    # Puntero al inicio para sorbeescribir
        fichero.seek(0)
        fichero.write("Palabra al inicio")
except Exception as e:
    print(f"Error: {e}")


# AGREGAR DATOS A UN ARCHIVO EXISTENTE (Al final)
try:
    with open('text.txt', 'a') as fichero:
        fichero.write("Nueva linea\n")
        fichero.close()
except Exception as e:
    print(f"Error: {e}")


# AGREGAR DATOS A UN ARCHIVO EXISTENTE O NO (Al final)
try:
    with open('text.txt', 'a+') as fichero:
        fichero.write("Nueva linea\n")
        fichero.close()
except Exception as e:
    print(f"Error: {e}")


# MODIFICAR CONTENIDO EN UN FICHERO
try:
    with open('text.txt', 'r+') as fichero:
        lineas = fichero.readlines()

        lineaAModificar = 3
        if 0 <= lineaAModificar < len(lineas):
            lineas[lineaAModificar] = "Modificacion\n"

        fichero.seek(0)
        fichero.writelines(lineas)
        fichero.truncate()

except Exception as e:
    print(f"Error: {e}")


# ELIMINAR UNA LINEA
try:
    with open('text.txt', 'r') as fichero:
        linea = fichero.readlines()

        lineaABorrar = 3

        if 0 <= lineaABorrar < len(linea):
            del linea[lineaABorrar]

        fichero.seek(0)
        fichero.writelines(lineas)
        fichero.truncate()
except Exception as e:
    print(f"Error: {e}")
