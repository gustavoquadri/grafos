import heapq

pontos = [
    "Igreja Santo Antonio",
    "Igreja Matriz Cristo Rei",
    "Capela Santa Catarina",
    "Igreja Sao Bento",
    "Praca Centenario",
    "Cemiterio Municipal",
    "Shopping Lamerica",
    "Mercado Apolo da Praca Vico",
    "The Best Acai",
    "Escola Sagrado",
    "UPA",
    "Rodoviaria Bento",
    "Dallonder Grande Hotel"
]

igrejas = [
    "Igreja Santo Antonio",
    "Igreja Matriz Cristo Rei",
    "Capela Santa Catarina",
    "Igreja Sao Bento"
]

grafo = {
    "Igreja Santo Antonio": [
        ("Praca Centenario", 0.95),
        ("Shopping Lamerica", 1.3),
        ("Mercado Apolo da Praca Vico", 0.9),
        ("Escola Sagrado", 1.1),
        ("Rodoviaria Bento", 0.65)
    ],

    "Igreja Matriz Cristo Rei": [
        ("Praca Centenario", 0.55),
        ("Shopping Lamerica", 1.2),
        ("The Best Acai", 1.4),
        ("Escola Sagrado", 0.7),
        ("UPA", 1.2)
    ],

    "Capela Santa Catarina": [
        ("Cemiterio Municipal", 1.0),
        ("The Best Acai", 1.8),
        ("Dallonder Grande Hotel", 1.0)
    ],

    "Igreja Sao Bento": [
        ("Cemiterio Municipal", 1.5),
        ("Shopping Lamerica", 0.75),
        ("Mercado Apolo da Praca Vico", 1.2),
        ("The Best Acai", 0.65),
        ("Dallonder Grande Hotel", 0.5)
    ],

    "Praca Centenario": [
        ("Igreja Santo Antonio", 0.95),
        ("Igreja Matriz Cristo Rei", 0.55),
        ("Escola Sagrado", 0.7),
        ("Shopping Lamerica", 0.95),
        ("Mercado Apolo da Praca Vico", 1.2),
        ("Rodoviaria Bento", 1.4)
    ],

    "Cemiterio Municipal": [
        ("Capela Santa Catarina", 1.0),
        ("Igreja Sao Bento", 1.5),
        ("Mercado Apolo da Praca Vico", 1.0),
        ("Dallonder Grande Hotel", 1.1)
    ],

    "Shopping Lamerica": [
        ("Igreja Santo Antonio", 1.3),
        ("Igreja Matriz Cristo Rei", 1.2),
        ("Igreja Sao Bento", 0.75),
        ("Praca Centenario", 0.95),
        ("The Best Acai", 0.4),
        ("Mercado Apolo da Praca Vico", 0.75),
        ("UPA", 1.5),
        ("Dallonder Grande Hotel", 1.2)
    ],

    "Mercado Apolo da Praca Vico": [
        ("Igreja Santo Antonio", 0.9),
        ("Igreja Sao Bento", 1.2),
        ("Praca Centenario", 1.2),
        ("Cemiterio Municipal", 1.0),
        ("Shopping Lamerica", 0.75),
        ("The Best Acai", 0.55),
        ("Rodoviaria Bento", 1.6)
    ],

    "The Best Acai": [
        ("Igreja Matriz Cristo Rei", 1.4),
        ("Capela Santa Catarina", 1.8),
        ("Igreja Sao Bento", 0.65),
        ("Shopping Lamerica", 0.4),
        ("Mercado Apolo da Praca Vico", 0.55),
        ("Dallonder Grande Hotel", 0.9)
    ],

    "Escola Sagrado": [
        ("Igreja Santo Antonio", 1.1),
        ("Igreja Matriz Cristo Rei", 0.7),
        ("Praca Centenario", 0.7),
        ("Rodoviaria Bento", 1.2),
        ("UPA", 1.7)
    ],

    "UPA": [
        ("Igreja Matriz Cristo Rei", 1.2),
        ("Shopping Lamerica", 1.5),
        ("Escola Sagrado", 1.7)
    ],

    "Rodoviaria Bento": [
        ("Igreja Santo Antonio", 0.65),
        ("Praca Centenario", 1.4),
        ("Mercado Apolo da Praca Vico", 1.6),
        ("Escola Sagrado", 1.2)
    ],

    "Dallonder Grande Hotel": [
        ("Capela Santa Catarina", 1.0),
        ("Igreja Sao Bento", 0.5),
        ("Cemiterio Municipal", 1.1),
        ("Shopping Lamerica", 1.2),
        ("The Best Acai", 0.9)
    ]
}


def ucs(grafo, inicio, objetivo):
    fila = [(0, inicio, [inicio])]
    menores_custos = {inicio: 0}

    while fila:
        custo_atual, no_atual, caminho = heapq.heappop(fila)

        if no_atual == objetivo:
            return caminho, custo_atual

        for vizinho, peso in grafo[no_atual]:
            novo_custo = custo_atual + peso

            if vizinho not in menores_custos or novo_custo < menores_custos[vizinho]:
                menores_custos[vizinho] = novo_custo
                novo_caminho = caminho + [vizinho]
                heapq.heappush(fila, (novo_custo, vizinho, novo_caminho))

    return None, float("inf")


def escolher_opcao(lista, mensagem):
    print(f"\n{mensagem}")
    for i, item in enumerate(lista, start=1):
        print(f"{i}. {item}")

    while True:
        try:
            opcao = int(input("Digite o numero da opcao: "))
            if 1 <= opcao <= len(lista):
                return lista[opcao - 1]
            else:
                print("Opcao invalida. Tente novamente.")
        except ValueError:
            print("Digite apenas numeros.")


def menu():
    while True:
        print("=" * 50)
        print("BUSCA UCS")
        print("=" * 50)

        origem = escolher_opcao(pontos, "Escolha seu ponto de partida:")
        destino = escolher_opcao(igrejas, "Escolha a igreja que deseja visitar:")

        caminho, custo = ucs(grafo, origem, destino)

        print("\n" + "-" * 50)
        if caminho:
            print("Melhor caminho encontrado:")
            print(" -> ".join(caminho))
            print(f"Custo total: {custo:.2f} km")
        else:
            print("Nao foi possivel encontrar um caminho.")
        print("-" * 50)

        continuar = input("\nDeseja fazer outra busca? (s/n): ").strip().lower()
        if continuar != "s":
            print("Encerrando o programa...")
            break


if __name__ == '__main__':
  menu()