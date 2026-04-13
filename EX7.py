ano = int(input("Digite o seu ano de nascimento: "))
if 2026 - ano >= 16 and 2026 - ano < 18 or 2026 - ano > 70:
    print("Seu voto é opcional esse ano")
elif 2026 - ano < 18:
    print("Seu voto é proibido esse ano")
else:
    print("Seu voto é obrigatório esse ano")

