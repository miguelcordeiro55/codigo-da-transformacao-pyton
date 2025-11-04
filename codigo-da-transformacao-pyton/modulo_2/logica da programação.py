"""
logica programaçao 
para plataforma vocação
nele vai conter operações matematicas
comparaçao de numeros
classficação por idade
"""


# Exercício 1
print("=== Operações Matemáticas ===")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print(f"Soma: {num1 + num2}")
print(f"Subtração: {num1 - num2}")
print(f"Multiplicação: {num1 * num2}")
print(f"Divisão: {num1 / num2}")
print(f"Resto da divisão (%): {num1 % num2}")

# Exercício 2
print("\n=== Comparação de Números ===")

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if a > b:
    print(f"O número {a} é maior que {b}.")
elif b > a:
    print(f"O número {b} é maior que {a}.")
else:
    print("Os dois números são iguais.")


# Exercício 3
print("\n=== Classificação por Idade ===")

idade = int(input("Digite a idade da pessoa: "))

if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")

