def cadastrar_produto(produtos: list, contador_produtos: int) -> tuple:
    """
    Função para cadastrar um novo produto na lista de produtos cadastrados.
    """

    nome = input("Nome do produto: ").strip()
    marca = input("Marca do produto: ").strip()
    modelo = input("Modelo do produto: ").strip()
    preco = float(input("Preço do produto: "))
    quantidade = int(input("Quantidade: "))

    produto = {
        "id": contador_produtos + 1,
        "nome": nome,
        "marca": marca,
        "modelo": modelo,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)
    contador_produtos += 1

    print(f"Produto '{nome}' cadastrado com sucesso!")
    print(f"Contador de produtos: {contador_produtos}")

    return produtos, contador_produtos


def consultar_produtos(produtos: list, contador_produtos: int) -> None:
    """
    Exibe todos os produtos cadastrados e
    o total de itens no ERP.
    """

    print("\n--- PRODUTOS CADASTRADOS ---")

    if contador_produtos == 0:
        print("Nenhum produto cadastrado ainda.")
    else:
        for indice, item in enumerate(produtos, start=1):
            print(
                f"{indice}. {item['nome']} - "
                f"R$ {item['preco']:.2f} - "
                f"Quantidade: {item['quantidade']}"
            )

    print(f"Total de produtos: {contador_produtos}")
    print("----------------------------------------\n")


# --- PROGRAMA PRINCIPAL (MENU DO ERP) --- #

lista_produtos = []
total_cadastrados = 0

while True:
    print("\n===== MENU DO ERP =====")
    print("1 - Cadastrar produto")
    print("2 - Consultar produtos")
    print("3 - Ver documentação (help)")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        lista_produtos, total_cadastrados = cadastrar_produto(
            lista_produtos, total_cadastrados
        )

    elif opcao == "2":
        consultar_produtos(lista_produtos, total_cadastrados)

    elif opcao == "3":
        help(cadastrar_produto)
        help(consultar_produtos)

    elif opcao == "0":
        print("Encerrando o ERP...")
        break

    else:
        print("Opção inválida! Tente novamente.")