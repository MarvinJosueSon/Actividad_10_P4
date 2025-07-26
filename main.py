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


def imprimirCuentaRegresiva(numero):
    if numero<=0:
        return numero
    else:
        print(numero)
        return imprimirCuentaRegresiva(numero-1)
imprimirCuentaRegresiva(10)



