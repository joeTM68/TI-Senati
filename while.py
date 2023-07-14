bandera=True
while bandera:
    try:
        numero = int(input('Ingrese solo numeros: '))
        print(numero)
        bandera=False
    except ValueError as e:
        print("usted escribio una letra")
