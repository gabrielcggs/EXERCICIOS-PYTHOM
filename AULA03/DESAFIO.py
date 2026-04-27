idade = int(input("Digite sua idade: "))
if idade >= 16 and idade < 18 or idade > 70:
    print("Seu voto é opcional")
elif idade < 18:
    print("Você não pode votar")
else:
    print("Seu voto é obrigatório")