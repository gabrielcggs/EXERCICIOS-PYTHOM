salario = float(input("Digite o seu salário:"))
reajuste_1 = salario * 1.2
reajuste_2 = salario * 1.15
reajuste_3 = salario * 1.1
reajuste_4 = salario * 1.05
if salario <= 280:
    print(f"Salário antes do reajuste: R$ {salario:.2f}")
    print("Percentual de aumento: 20%")
    print(f"Valor de aumento: R$ {reajuste_1 - salario:.2f}")
    print(f"Novo salário: R$ {reajuste_1:.2f}")
elif 280 <= salario < 700:
    print(f"Salário antes do reajuste: R$ {salario:.2f}")
    print("Percentual de aumento: 15%")
    print(f"Valor de aumento: R$ {reajuste_2 - salario:.2f}")
    print(f"Novo salário: R$ {reajuste_2:.2f}")
elif 700 <= salario < 1500:
    print(f"Salário antes do reajuste: R$ {salario:.2f}")
    print("Percentual de aumento: 10%")
    print(f"Valor de aumento: R$ {reajuste_3 - salario:.2f}")
    print(f"Novo salário: R$ {reajuste_3:.2f}")
else:
    print(f"Salário antes do reajuste: R$ {salario:.2f}")
    print("Percentual de aumento: 5%")
    print(f"Valor de aumento: R$ {reajuste_4 - salario:.2f}")
    print(f"Novo salário: R$ {reajuste_4:.2f}")