print("Digite o numero de quadrados perfeitos que você irá querer: ")
a = int(input(">>>")) + 1
b = list(range( 1,a))
for a in b:
    print(a**2)
    a += 1
