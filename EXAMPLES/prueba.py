
"""
texto = "Hola mundo"

try:
    with open("texto.txt", "r") as fichero:
        text_leer = fichero.read()
        print(text_leer)
        fichero.close()

except FileNotFoundError:
    pass

try:
    with open("texto.txt", "w") as fichero:
        fichero.write(texto)
        fichero.close()

except FileNotFoundError:
    pass


try:
    with open("texto.txt", "a+") as fichero:
        fichero.write(texto + "\n")

except FileNotFoundError:
    print("Error")



try:
    with open("texto.txt", "r+") as fichero:
        lineas = fichero.readlines()

        lineaABorrar = 0
        if 0 <= lineaABorrar < len(lineas):
            del lineas[lineaABorrar]

        fichero.seek(0)
        fichero.writelines(lineas)
        fichero.truncate()
except ValueError:
    pass

try:
    with open("texto.txt", "a+") as fichero:
        fichero.write("Lalo\n")
        fichero.close()
except ValueError:
    pass


try:
    with open("texto.txt", "r+") as fichero:
        lineas = fichero.readlines()

        lineaAModificar = 8
        if 0 <= lineaAModificar < len(lineas):
            lineas[lineaAModificar] = "Sab\n"

        fichero.seek(0)
        fichero.writelines(lineas)
        fichero.truncate()
except ValueError:
    pass
"""


def cargar(lista):
    try:
        with open("texto.txt", "r") as tareas_txt:
            for tarea_txt in tareas_txt:
                tarea = tarea_txt.strip().split(";")
                lista.append(tarea)

    except FileNotFoundError:
        print("No se encontró el fichero")


def resumen(lista):
    minCompletados = 0
    cantFallidas = 0
    for registro in lista:
        if registro[3] == "completada":
            minCompletados += registro[1]

        else:
            cantFallidas += 1

    totalmin = f"Total: {minCompletados}"
    fallidas = f"Fallidas: {cantFallidas}"
    return totalmin, fallidas


def cargarResumen(lista):
    totalmnin, fallidas = resumen(lista)
    with open("resumen", "w") as registros:
        registros.write(totalmnin+"\n"+fallidas)
        registros.close()


def cantCompletadas(lista):
    com = input("Ingrese tel a buscar: ")
    cantCom = 0
    encontrada = False
    for registro in lista:
        if registro[2] == com:
            if registro[3] == "completado":
                cantCom += 1

    print(f"Cant encontrada: {cantCom}")
    if not encontrada:
        print("NO encontrada")


def mostrarMenor(lista):
    indice = 0
    menor = lista[0][1]
    for i in range(1, len(lista)):
        if lista[i][1] < menor:
            indice = i

    print(lista[indice])


def main():
    lista = []
    cargar(lista)
    cargarResumen(lista)
    mostrarMenor(lista)


main()
