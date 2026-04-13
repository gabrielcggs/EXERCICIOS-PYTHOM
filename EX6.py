num_1 = int(input("Digite um número: "))
num_2 = int(input("Digite outro número: "))
caractere = input("Digite um caractere que representa uma operação matemática(+, -, *, /): ")

if caractere == "+":
    print(num_1 + num_2)
elif caractere == "-":
    print(num_1 - num_2)
elif caractere == "*":
    print(num_1 * num_2)
else:
    print(num_1 / num_2)