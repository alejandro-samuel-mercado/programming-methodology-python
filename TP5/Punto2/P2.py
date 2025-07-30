from io import open
import re


def validarNombre(mensaje):
    patron = r'^[a-zA-Z/ +-_]+$'
    while True:
        nombre = input(f"""Ingrese {mensaje}""")
        if len(nombre) != 0:
            if re.match(patron, nombre):
                break
            else:
                print("Nombre no válido")
        else:
            print("No puede estar vacío")

    return nombre


def leerFichero():
    libros = []
    try:
        fichero = open('./libros.txt', 'r')
        for libro_txt in fichero:
            libro = libro_txt.strip().split(",")
            libros.append([libro[0], libro[1], libro[2],
                           libro[3], libro[4], libro[5], libro[6]])
    except FileNotFoundError:
        print("No se encuentra el directorio")
    return libros


def mostrarLibros(libros):

    print(libros)


def busquedaBinaria(libros, elementoBuscar):

    izq = 0  # izq guarda el índice inicio del segmento
    der = len(libros) - 1  # der guarda el índice fin del segmento

    # un segmento es vacío cuando izq > der:
    while izq <= der:
        medio = (izq+der)//2
        elemento = libros[medio][1].strip().lower()
        if elemento == elementoBuscar:
            return medio
        elif elemento > elementoBuscar:
            der = medio-1
        else:
            izq = medio+1
    return -1


def buscarPorTitulo(libros):
    tituloBuscar = validarNombre("el titulo del libro a buscar: ")
    posElementoEncontrado = busquedaBinaria(libros, tituloBuscar)
    if posElementoEncontrado != -1:
        print(libros[posElementoEncontrado])
    else:
        print("Libro no encontrado")


def buscarPorGenero(libros):
    generoBuscar = validarNombre("el género del libro a buscar: ").lower()
    encontrado = False

    for libro in libros:
        genero = libro[3].strip().lower()
        if generoBuscar == genero or generoBuscar[:3] == genero[:3]:
            print(libro)
            encontrado = True
            break

    if not encontrado:
        print("Libro no encontrado")


def shellSort(lista):
    n = len(lista)
    gap = n//2

    while gap > 0:
        for i in range(gap, n):
            tmp = lista[i]
            j = i
            while j >= gap and lista[j-gap][5] > tmp[5]:
                lista[j] = lista[j-gap]
                j -= gap
            lista[j] = tmp
        gap = gap//2


def listaPorAutor(libros):
    autorBuscado = validarNombre("el autor a buscar: ").strip().lower()
    listaSegunAutor = []
    for libro in libros:
        autor = libro[2].strip().lower()
        if autor == autorBuscado:
            listaSegunAutor.append(libro)

    shellSort(listaSegunAutor)
    print(listaSegunAutor)


def validarNum(mensaje):
    while True:
        try:
            num = float(input(f"""Ingrese {mensaje}"""))
            break
        except ValueError:
            print("Error. Ingrese un valor válido")
    return num


def listarPorPrecio(libros):
    listarPorPrecio = []
    min = validarNum("rango mínimo: ")
    max = validarNum("rango máximo: ")

    for libro in libros:
        precio = float(libro[5])
        if min <= precio <= max:
            listarPorPrecio.append(libro)

    shellSort(listarPorPrecio)
    print(listarPorPrecio)


def modificarPrecioP(libros):
    for libro in libros:
        estado = libro[6].strip().lower()
        if estado == "p":
            precio = float(libro[5])
            precio = precio+round(precio*0.15, 2)
            libro[5] = precio


def main():
    libros = leerFichero()
    while True:
        try:
            op = int(input("""Ingrese una opción:
        1-Mostrar libros
        2-Buscar libro por titulo
        3-Buscar libro por genero
        4-Mostrar libros escritos por autor
        5-Mostrar libros que estén entre cierto precio
        6-Modificar libro en estado de pedido
        7-Salir
        ---------------------\n"""))

        except ValueError:
            print("Ingrese una opción válida")

        if op:
            if op == 1:
                mostrarLibros(libros)

            elif op == 2:
                buscarPorTitulo(libros)

            elif op == 3:
                buscarPorGenero(libros)

            elif op == 4:
                listaPorAutor(libros)

            elif op == 5:
                listarPorPrecio(libros)

            elif op == 6:
                modificarPrecioP(libros)

            elif op == 7:
                print("Saliendo...")
                break


main()
