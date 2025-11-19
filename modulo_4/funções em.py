# 1️⃣ Função de saudação personalizada
def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a)!")


# 2️⃣ Função para calcular média e dizer se foi aprovado
def calcular_media(notas):
    media = sum(notas) / len(notas)
    if media >= 7:
        print(f"Média: {media:.2f} - Aluno APROVADO")
    else:
        print(f"Média: {media:.2f} - Aluno REPROVADO")


# 3️⃣ Função que retorna o maior e o menor número de uma lista
def maior_menor(lista):
    maior = max(lista)
    menor = min(lista)
    return maior, menor


# ⭐ Desafio Extra: sistema simples de login
def sistema_login(usuarios):
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login realizado com sucesso!")
    else:
        print("Usuário ou senha incorretos.")


# -------------------------
# Exemplos de uso:
# -------------------------

# 1
saudacao("Maria")

# 2
notas_aluno = [8.5, 7.0, 6.0]
calcular_media(notas_aluno)

# 3
numeros = [3, 10, 2, 50, -4]
maior, menor = maior_menor(numeros)
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")

# Desafio Extra
usuarios_cadastrados = {
    "admin": "1234",
    "joao": "senha123"
}

sistema_login(usuarios_cadastrados)