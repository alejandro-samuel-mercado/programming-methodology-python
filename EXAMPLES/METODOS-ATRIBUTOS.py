cad = "hoalaa"
print(cad.find("o"))  # 1
print(cad.rfind("a"))  # 4
print(cad.replace("a", "l"))  # hollll

word = "n a n c y"
separar = word.split(" ")
print(separar)  # [n, a, n, c, y]

word1 = ["s", "o", "f", "i"]
unir = "".join(word1)
print(unir)  # sofi

# String a número
word2 = "b"
convertir = ord(word2)
print(convertir)  # 98

# Número a string
num = 2
conv = chr(num)
print(conv)  # c

# - capitalize()  Convierte el primer carácter de una cadena en mayúscula y el resto en minúsculas
# - endswith("") Devuelve True si la cadena termina con el sufijo especificado
# – format() Permite formatear cadenas e insertar valores en marcadores de posición {}
mensaje = "Hola, {}. Tienes {} mensajes nuevos."
print(mensaje.format("Juan", 5))  # "Hola, Juan. Tienes 5 mensajes nuevos."

# – isalnum() Devuelve True si todos los caracteres en la cadena son alfanuméricos (letras o números) y no hay espacios ni caracteres especiales
# – isalpha() Devuelve True si todos los caracteres de la cadena son letras y no hay números ni espacios
# – isdigit() Devuelve True si todos los caracteres de la cadena son números enteros
# – isnumeric() Devuelve True si todos los caracteres de la cadena son caracteres numéricos (incluye dígitos y caracteres como fracciones o números romanos).
# – isspace() Devuelve True si la cadena solo contiene caracteres de espacio en blanco
# – print(dir(str))  # todos los métodos de str
