from operator import truediv


def cant_vc(n):
    cantidad_vocales=0
    cantidad_consonantes=0
    n = n.lower=()
    for letra in n:
        if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u": 
            cantidad_vocales += 1
        else:
            cantidad_consonantes += 1
    r = f"""Nombre: {n} 
            Numero de vocales: {cantidad_vocales}
            Numero de consonantes: { cantidad_consonantes}
            Numero de letras:  { len(n)}"""
    return r
lista_nombres =[]
flag=true
while flag:
    nombres =imput("ingrese un nombre o para terminar escriba x")

    if cnombres == "x":
        flag=False
    else:
        nombre =nombres.capitalize()     
        if cnombre in lista_cmbres:
            pass
        else:
            lista_nombres.append(cnombre)