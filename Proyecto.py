# PROYECTO LÓGICA: Katas de Python

# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencia_letras(cadena):
    frecuencias = {}
    
    for letra in cadena:
        if letra != " ":  
            letra = letra.lower() 
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1
                
    return frecuencias

texto = "Hola, vamos a probar que la frecuencia sea correcta"
resultado = frecuencia_letras(texto)
print(resultado)

# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

def duplicar_lista(lista):
    return list(map(lambda x: x * 2, lista))

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = duplicar_lista(numeros)
print(resultado)

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def buscar_palabras(lista_palabras, palabra_objetivo):
    resultado = []
    
    for palabra in lista_palabras:
        if palabra_objetivo in palabra:
            resultado.append(palabra)
    
    return resultado

palabras = ["programacion", "programa", "progreso", "gato", "pro"]
objetivo = "pro"

print(buscar_palabras(palabras, objetivo))

# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def diferencia_listas(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))

lista1 = [10, 20, 30, 40, 50]
lista2 = [1, 2, 3, 4, 5]

resultado = diferencia_listas(lista1, lista2)
print(resultado)

# 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

def calcular_resultado(lista_notas, nota_aprobado=5):
    media = sum(lista_notas) / len(lista_notas)
    
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
    
    return (media, estado)

notas = [6, 7, 5, 8, 3, 1]
resultado = calcular_resultado(notas)
print(resultado)

# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4))

# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tuplas_a_strings(lista_tuplas):
    return list(map(str, lista_tuplas))

tuplas = [(0, 1), (2, 3), (4, 5)]
resultado = tuplas_a_strings(tuplas)
print(resultado)

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.


def dividir_numeros():
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        
        resultado = num1 / num2
        
    except ValueError:
        print("Error: Debes introducir valores numéricos.")
    
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    
    else:
        print("La división fue exitosa.")
        print("Resultado:", resultado)
    
    finally:
        print("Fin del programa.")

dividir_numeros()

# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()


def filtrar_mascotas(lista_mascotas):
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    
    return list(filter(lambda mascota: mascota not in mascotas_prohibidas, lista_mascotas))

mascotas = ["Perro", "Gato", "Mapache", "Oso", "Cocodrilo", "Hamster"]

resultado = filtrar_mascotas(mascotas)
print(resultado)

# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

class ListaVaciaError(Exception):
    pass

def calcular_promedio_lista(lista):
    if len(lista) == 0:
        raise ListaVaciaError("La lista está vacía, no se puede calcular el promedio.")
    return sum(lista) / len(lista)

try:
    numeros = [4, 6, 7]
    promedio = calcular_promedio_lista(numeros)
    print("Promedio:", promedio)

except ListaVaciaError as e:
    print("Error:", e)

else:
    print("Cálculo realizado correctamente.")

finally:
    print("Fin del programa.")

# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

try:
    edad = int(input("Introduce tu edad: "))
    
    if edad < 0 or edad > 120:
        raise ValueError("La edad debe estar entre 0 y 120 años.")
    
except ValueError as e:
    print("Error:", e)

else:
    print("Edad válida:", edad)

finally:
    print("Fin del programa.")

# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitud_palabras(frase):
    palabras = frase.split()
    return list(map(len, palabras))

texto = "Hola vamos a probar este código"
resultado = longitud_palabras(texto)
print(resultado)

# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map()

def letras_mayus_minus(caracteres):
    conjunto_unico = set(caracteres)
    
    return list(map(lambda c: (c.upper(), c.lower()), conjunto_unico))

texto = "aAbBcaZzZz"
resultado = letras_mayus_minus(texto)
print(resultado)

# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

def filtrar_por_letra(lista_palabras, letra):
    return list(filter(lambda palabra: palabra.startswith(letra), lista_palabras))

palabras = ["Perro", "Gato", "Mapache", "Oso", "Cocodrilo", "Hamster"]
resultado = filtrar_por_letra(palabras, "P")
print(resultado)

# 15. Crea una función lambda que sume 3 a cada número de una lista dada.

sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))

numeros = [1, 2, 3, 4, 5]
resultado = sumar_tres(numeros)
print(resultado)

# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

def palabras_mas_largas(texto, n):
    palabras = texto.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))

frase = "Vamos a probar si alguna palabra lo cumple"
resultado = palabras_mas_largas(frase, 5)
print(resultado)

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()

from functools import reduce

def lista_a_numero(lista_digitos):
    return reduce(lambda acumulado, digito: acumulado * 10 + digito, lista_digitos)

digitos = [5, 7, 2, 1]
resultado = lista_a_numero(digitos)
print(resultado)

# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

estudiantes = [
    {"nombre": "Alejandro", "edad": 20, "calificacion": 65},
    {"nombre": "Luis", "edad": 22, "calificacion": 85},
    {"nombre": "Marta", "edad": 19, "calificacion": 90},
    {"nombre": "Carlos", "edad": 21, "calificacion": 88},
    {"nombre": "Sofía", "edad": 23, "calificacion": 100}
]

# Usamos filter() para obtener estudiantes con calificación >= 90
estudiantes_destacados = list(
    filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes)
)

print(estudiantes_destacados)

# 19. Crea una función lambda que filtre los números impares de una lista dada.

filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = filtrar_impares(numeros)
print(resultado)

# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

def filtrar_enteros(lista):
    return list(filter(lambda elemento: isinstance(elemento, int), lista))

datos = [1, "hola", 3, "probando", 5, "como", 8, "funciona", 10]
resultado = filtrar_enteros(datos)
print(resultado)

# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

calcular_cubo = lambda x: x ** 3

resultado = calcular_cubo(3)
print(resultado)

# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .

def producto_total(lista):
    return reduce(lambda acumulado, x: acumulado * x, lista)

numeros = [2, 3, 4, 5]
resultado = producto_total(numeros)
print(resultado)

# 23. Concatena una lista de palabras. Usa la función reduce() .

def concatenar_palabras(lista_palabras):
    return "".join(lista_palabras)

palabras = ["Hola", " ", "probando", " ", "como"," ", "funciona"]
resultado = concatenar_palabras(palabras)
print(resultado)

# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .

from functools import reduce

def diferencia_total(lista):
    return reduce(lambda acumulado, x: acumulado - x, lista)

numeros = [8, 2, 3]
resultado = diferencia_total(numeros)
print(resultado)

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(texto):
    return len(texto)

frase = "Probando que funciona"
resultado = contar_caracteres(frase)
print(resultado)

# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

calcular_resto = lambda a, b: a % b

resultado = calcular_resto(11, 3)
print(resultado)

# 27. Crea una función que calcule el promedio de una lista de números.

def calcular_promedio_simple(lista):
    return sum(lista) / len(lista)

numeros = [5, 7, 2, 7]
resultado = calcular_promedio_simple(numeros)
print(resultado)

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    vistos = set()
    
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    
    return None

numeros = [3, 5, 7, 2, 5, 8]
resultado = primer_duplicado(numeros)
print(resultado)

# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.

def enmascarar_variable(valor):
    texto = str(valor)
    
    if len(texto) <= 4:
        return texto
    
    return "#" * (len(texto) - 4) + texto[-4:]

dato = 123456789
resultado = enmascarar_variable(dato)
print(resultado)

# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def son_anagramas(palabra1, palabra2):
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()
    
    return sorted(palabra1) == sorted(palabra2)

print(son_anagramas("roma", "amor"))

# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

def buscar_nombre():
    try:
        entrada = input("Introduce una lista de nombres separados por coma: ")
        lista_nombres = [nombre.strip() for nombre in entrada.split(",")]
        
        nombre_buscar = input("Introduce el nombre a buscar: ").strip()
        
        if nombre_buscar in lista_nombres:
            print(f"El nombre '{nombre_buscar}' fue encontrado en la lista.")
        else:
            raise ValueError(f"El nombre '{nombre_buscar}' no está en la lista.")
    
    except ValueError as e:
        print("Error:", e)
    
    finally:
        print("Fin del programa.")

buscar_nombre()

# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def buscar_empleado(nombre_completo, lista_empleados):
    for empleado in lista_empleados:
        if empleado["nombre"] == nombre_completo:
            return empleado["puesto"]
    
    return "La persona no trabaja aquí."

empleados = [
    {"nombre": "Ana López", "puesto": "Gerente"},
    {"nombre": "Luis García", "puesto": "Desarrollador"},
    {"nombre": "Marta Pérez", "puesto": "Diseñadora"}
]

resultado = buscar_empleado("Luis García", empleados)
print(resultado)

# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

resultado = sumar_listas(lista1, lista2)
print(resultado)

# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.

class Arbol:

    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco = self.tronco + 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        # Lo hacemos con un for normal
        for i in range(len(self.ramas)):
            self.ramas[i] = self.ramas[i] + 1

    def quitar_rama(self, posicion):
        # Sin validaciones complicadas
        if posicion >= 0 and posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            raise IndexError("No existe esa rama")

    def info_arbol(self):
        print("Longitud del tronco:", self.tronco)
        print("Número de ramas:", len(self.ramas))
        print("Longitudes de las ramas:", self.ramas)


# Caso de uso

arbol = Arbol()

arbol.crecer_tronco()

arbol.nueva_rama()

arbol.crecer_ramas()

arbol.nueva_rama()
arbol.nueva_rama()

arbol.quitar_rama(2)

arbol.info_arbol()

# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.

class UsuarioBanco:

    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if not self.cuenta_corriente:
            raise ValueError("El usuario no tiene cuenta corriente")

        if cantidad > self.saldo:
            raise ValueError("No hay suficiente saldo")

        self.saldo = self.saldo - cantidad
        print(self.nombre, "ha retirado", cantidad)

    def transferir_dinero(self, otro_usuario, cantidad):
        if not self.cuenta_corriente:
            raise ValueError("El usuario no tiene cuenta corriente")

        if cantidad > self.saldo:
            raise ValueError("No hay suficiente saldo para transferir")

        # Restamos al usuario actual
        self.saldo = self.saldo - cantidad

        # Sumamos al otro usuario
        otro_usuario.saldo = otro_usuario.saldo + cantidad

        print(self.nombre, "ha transferido", cantidad, "a", otro_usuario.nombre)

    def agregar_dinero(self, cantidad):
        self.saldo = self.saldo + cantidad
        print("Se agregaron", cantidad, "a", self.nombre)

    def info(self):
        print("Nombre:", self.nombre)
        print("Saldo:", self.saldo)
        print("Cuenta corriente:", self.cuenta_corriente)
        print("-------------------")

# 1. Crear usuarios
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# 2. Agregar 20 a Bob
bob.agregar_dinero(20)

# 3. Transferir 80 desde Bob a Alicia
bob.transferir_dinero(alicia, 80)

# 4. Retirar 50 de Alicia
alicia.retirar_dinero(50)

# Mostrar información final
alicia.info()
bob.info()


# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras , reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto .

# 1 Contar palabras
def contar_palabras(texto):
    palabras = texto.split()
    contador = {}

    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1

    return contador


# 2️ Reemplazar palabras
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)


# 3️ Eliminar palabra
def eliminar_palabra(texto, palabra):
    palabras = texto.split()
    nueva_lista = []

    for p in palabras:
        if p != palabra:
            nueva_lista.append(p)

    return " ".join(nueva_lista)


# 4️ Función principal
def procesar_texto(texto, opcion, *args):

    if opcion == "contar":
        return contar_palabras(texto)

    elif opcion == "reemplazar":
        if len(args) != 2:
            return "Faltan argumentos para reemplazar"
        return reemplazar_palabras(texto, args[0], args[1])

    elif opcion == "eliminar":
        if len(args) != 1:
            return "Faltan argumentos para eliminar"
        return eliminar_palabra(texto, args[0])

    else:
        return "Opción no válida"


texto = "probando como funciona la funcion"

# Contar palabras
print(procesar_texto(texto, "contar"))

# Reemplazar palabra
print(procesar_texto(texto, "reemplazar", "funciona", "sí funciona"))

# Eliminar palabra
print(procesar_texto(texto, "eliminar", "probando"))

# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

try:
    hora = int(input("Introduce la hora (0-23): "))

    if hora < 0 or hora > 23:
        print("Hora no válida")

    elif hora >= 6 and hora < 12:
        print("Es de día")

    elif hora >= 12 and hora < 20:
        print("Es tarde")

    else:
        print("Es de noche")

except ValueError:
    print("Debes introducir un número válido")

# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.

try:
    nota = int(input("Introduce la calificación (0-100): "))

    if nota < 0 or nota > 100:
        print("Calificación no válida")

    elif nota <= 69:
        print("Insuficiente")

    elif nota <= 79:
        print("Bien")

    elif nota <= 89:
        print("Muy bien")

    else:
        print("Excelente")

except ValueError:
    print("Debes introducir un número válido")

# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math

def calcular_area(figura, datos):

    if figura == "rectangulo":
        base, altura = datos
        return base * altura

    elif figura == "circulo":
        radio = datos[0]
        return math.pi * radio * radio

    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2

    else:
        return "Figura no válida"

print(calcular_area("rectangulo", (5, 3)))
print(calcular_area("circulo", (4,)))
print(calcular_area("triangulo", (6, 2)))

# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento.

try:
    precio = float(input("Introduce el precio original del artículo: "))

    if precio < 0:
        print("El precio no puede ser negativo")

    else:
        cupon = input("¿Tienes cupón de descuento? (si/no): ").lower()

        if cupon == "si":
            descuento = float(input("Introduce el valor del cupón: "))

            if descuento > 0:
                precio_final = precio - descuento

                if precio_final < 0:
                    precio_final = 0

                print("Descuento aplicado.")
                print("Precio final:", precio_final, "€")

            else:
                print("El valor del cupón no es válido.")
                print("Precio final:", precio, "€")

        elif cupon == "no":
            print("No se aplicó descuento.")
            print("Precio final:", precio, "€")

        else:
            print("Respuesta no válida.")

except ValueError:
    print("Debes introducir un valor numérico válido.")


