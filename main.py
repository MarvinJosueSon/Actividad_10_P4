def contarDigitos(numero):
    if numero<10:
        return 1
    else:
        return 1+contarDigitos(numero//10)

contarDigitos(154)
print(contarDigitos(154))