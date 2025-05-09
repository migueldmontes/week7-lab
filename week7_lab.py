# 1. FRASE SALUDO ITERATIVO
def saludar():
    saludo = input("Escribe un saludo (ej. Hola, Adiós): ")
    nombre = input("Escribe un nombre (ej. Marga, Carol): ")
    return f"{saludo} {nombre}"

def ejecutar_saludos():
    veces = int(input("¿Cuántas veces quieres saludar? "))
    resultados = []
    for _ in range(veces):
        resultado = saludar()
        resultados.append(resultado)

    print("\n--- Saludos realizados ---")
    for linea in resultados:
        print(linea)

# 2. CÁLCULO OPERACIÓN A ELEGIR (SIN RETURN)
def sumar(a, b):
    print(f"Resultado de la suma: {a + b}")

def restar(a, b):
    print(f"Resultado de la resta: {a - b}")

def calculadora_sin_return():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    operacion = input("¿Qué quieres hacer? (+ o -): ")
    
    if operacion == "+":
        sumar(num1, num2)
    elif operacion == "-":
        restar(num1, num2)
    else:
        print("Operación no válida.")

# EXTRA: CON RETURN
def sumar_con_return(a, b):
    return a + b

def restar_con_return(a, b):
    return a - b

def calculadora_con_return():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    operacion = input("¿Qué quieres hacer? (+ o -): ")

    if operacion == "+":
        resultado = sumar_con_return(num1, num2)
        print(f"Resultado de la suma: {resultado}")
    elif operacion == "-":
        resultado = restar_con_return(num1, num2)
        print(f"Resultado de la resta: {resultado}")
    else:
        print("Operación no válida.")

# Ejecutar las funciones
if __name__ == "__main__":
    ejecutar_saludos()
    calculadora_sin_return()
    calculadora_con_return()
