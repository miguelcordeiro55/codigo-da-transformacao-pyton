# ============================================================
# 🎓 EXERCÍCIO 2 – Dicionário de Aluno
# ============================================================
# Crie um dicionário que armazene informações como:
# nome, idade e notas de um aluno.
# Em seguida, exiba os dados armazenados no console.
# ============================================================

def exercicio_2_dicionario_aluno():
    print("\n--- Cadastro de Aluno ---")

    nome = input("Nome: ").strip()

    while True:
        try:
            idade = int(input("Idade: "))
            break
        except ValueError:
            print("Por favor, digite uma idade válida (número inteiro).")

    notas = []
    print("Digite as notas (pressione Enter sem digitar nada para encerrar):")
    while True:
        s = input("Nota: ").strip()
        if s == "":
            break
        try:
            notas.append(float(s))
        except ValueError:
            print("Por favor, digite um número válido para a nota.")

    aluno = {
        "nome": nome,
        "idade": idade,
        "notas": notas
    }

    print("\n--- Dados do Aluno ---")
    for chave, valor in aluno.items():
        print(f"{chave}: {valor}")


