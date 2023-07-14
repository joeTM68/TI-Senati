
flag1=True
flag2=True  
while flag1:
    try:
        a = int(input("Valor 1: "))
        flag1=False
    except ValueError:
        print("te equivocaste")
print(a)
while flag2:
    try:
        b = int(input("Valor 2: "))
        flag2=False
    except ValueError:
        print("te equivocaste")
print("b")
print(f"mi valores obtenidos son {a} {b}")

def die(x,y):
    if (x%y)==0:
        r=f"{x} / {y} es una divicion exacta"
    elif (x%y)==2:
        r=f"{x} / {y} es una divicion inexacta"
    return r

print(die(a,b))