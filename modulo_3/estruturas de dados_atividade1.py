# ============================================================
# 🧾 EXERCÍCIO 1 – Lista de Compras
# ============================================================
# Escreva um programa que gerencie uma lista de compras.
# O usuário deve poder adicionar itens, remover itens
# e visualizar a lista atualizada dinamicamente.
# ============================================================

def exercicio_1_lista_compras():
    compras = []

    while True:
        print("\n--- Lista de Compras ---")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Ver lista")
        print("4. Limpar lista")
        print("5. Voltar ao menu principal")

        opc = input("Escolha uma opção: ").strip()

        if opc == "1":
            item = input("Digite o item para adicionar: ").strip()
            if item:
                compras.append(item)
                print(f"'{item}' foi adicionado à lista.")
            else:
                print("Nenhum item inserido.")

        elif opc == "2":
            if not compras:
                print("A lista está vazia.")
                continue

            print("Itens na lista:")
            for i, it in enumerate(compras, 1):
                print(f"{i}. {it}")

            try:
                idx = int(input("Digite o número do item a remover: "))
                if 1 <= idx <= len(compras):
                    removido = compras.pop(idx - 1)
                    print(f"'{removido}' foi removido da lista.")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Entrada inválida, digite um número.")

        elif opc == "3":
            if compras:
                print("\nLista atual:")
                for i, it in enumerate(compras, 1):
                    print(f"{i}. {it}")
            else:
                print("A lista está vazia.")

        elif opc == "4":
            compras.clear()
            print("A lista foi limpa com sucesso.")

        elif opc == "5":
            break

        else:
            print("Opção inválida. Tente novamente.")

