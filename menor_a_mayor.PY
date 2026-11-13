#CLAUDE

a = int(input("Primer número: "))
b = int(input("Segundo número: "))
c = int(input("Tercer número: "))

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

print("De menor a mayor:", a, b, c)

#CHATGPT
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

if num1 <= num2 and num1 <= num3:
    if num2 <= num3:
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)
else:
    if num2 <= num1 and num2 <= num3:
        if num1 <= num3:
            print(num2, num1, num3)
        else:
            print(num2, num3, num1)
    else:
        if num1 <= num2:
            print(num3, num1, num2)
        else:
            print(num3, num2, num1)