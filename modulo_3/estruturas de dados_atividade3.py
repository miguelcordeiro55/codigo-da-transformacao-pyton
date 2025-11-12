
# ============================================================
# 🔢 EXERCÍCIO 3 – Números Pares e Ímpares
# ============================================================
# Dado um conjunto de números, use um loop para identificar
# quais são pares e quais são ímpares, exibindo cada categoria
# separadamente.
# ============================================================

def exercicio_3_pares_impares():
    print("\n--- Separar Números Pares e Ímpares ---")
    entrada = input("Digite números separados por espaço: ").strip()

    if entrada == "":
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print("Usando lista padrão:", numeros)
    else:
        try:
            numeros = [int(x) for x in entrada.split()]
        except ValueError:
            print("Entrada inválida. Usando lista padrão.")
            numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    pares = [n for n in numeros if n % 2 == 0]
    impares = [n for n in numeros if n % 2 != 0]

    print("\nNúmeros Pares:", pares)
    print("Números Ímpares:", impares)


