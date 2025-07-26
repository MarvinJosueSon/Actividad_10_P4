def contarDigitos(numero):
    if numero<10:
        return 1
    else:
        return 1+contarDigitos(numero//10)

def sumarDigitos(numero):
    if numero <= 0:
        return 0
    else:
        return numero % 10 + sumarDigitos(numero // 10)

def invertir(cadena):
    if len(cadena) == 0:
        return ""
    else:
        return cadena[-1] + invertir(cadena[:-1])
def imprimirCuentaRegresiva(numero):
    if numero<=0:
        return numero
    else:
        print(numero)
        return imprimirCuentaRegresiva(numero-1)

def Suma(numero):
    if numero==0:
        return 0
    else:
        return numero + Suma(numero-1)

while True:
    try:
        print("==MENU==")
        print("1. Invertir palabra")
        print("2. Suma de n numeros")
        print("3. Secuencia regresiva")
        print("4. Sumar digitos de un numero")
        print("5. Contar Digitos")
        print("6. Salir")
        opcion=input("Ingrese el numero de opcion: ")
        match opcion:
            case "1":
                palabra=input("Ingrese la palabra: ")
                print(f"Palabra invertida: {invertir(palabra)}")
            case "2":
                numero=int(input("Ingrese el numero: "))
                print(f"La suma de los numeros es: {Suma(numero)}")
            case "3":
                numero=int(input("Ingrese el numero: "))
                imprimirCuentaRegresiva(numero)
            case "4":
                numero=int(input("Ingrese un numero: "))
                print(f"La suma de los digitos es: {sumarDigitos(numero)}")
            case "5":
                numero=int(input("Ingrese el numero: "))
                print(f"La cantidad de digitos es: {contarDigitos(numero)}")
            case "6":
                print("Saliendo...")
    except ValueError:
        print("ERROR:")




