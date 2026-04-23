# Exercício 3:
# Crie uma aplicação que faz a gestão de estoque de uma empresa.
# Essa empresa precisa ter um produto,
# uma descrição para este produto, um número x de um dado produto,
# o valor unitário de cada produto e o valor total do estoque.
# O software deve permitir atualizarmos  o valor do produto (refletindo no valor total do estoque), atualizar a quantidade do produto em estoque,
# atualizar o nome do produto e atualizar a descrição deste produto.
# Por fim, o software deve permitir também que a gente possa ver essas informações.

nome_produto = str(input("Nome do produto: "))
desc_produto = str(input("Descrição do produto: "))
qtd_produto = int(input("Quantidade do produto: "))
valU_produto = float(input("Valor unitário do produto: "))
valor_total_estoque = qtd_produto * valU_produto

opcao = 0

while opcao != 6:
    print("[1] - Ver informações do produto")
    print("[2] - Atualizar nome do produto")
    print("[3] - Atualizar descrição do produto")
    print("[4] - Atualizar quantidade em estoque do produto")
    print("[5] - Atualizar valor unitário do produto")
    print("[6] - Sair")
    opcao = int(input("Opção desejada: "))
    if opcao == 1:
        print("================")
        print("Nome: ", nome_produto, " | Valor R$: ", valU_produto)
        print("Descrição: ", desc_produto, " | Qtd. Estoque: ", qtd_produto)
        print("Valor em estoque: ", valor_total_estoque)
    elif opcao == 2:
        nome_produto = str(input("Novo nome do produto: "))
    elif opcao == 3:
        desc_produto = str(input("Nova descrição do produto: "))
    elif opcao == 4:
        qtd_produto = int(input("Nova quantidade do produto: "))
        valor_total_estoque = qtd_produto * valU_produto
    elif opcao == 5:
        valU_produto = float(input("Novo valor unitário do produto: "))
        valor_total_estoque = qtd_produto * valU_produto
    elif opcao == 6:
        print("Saindo...")
    else:
        print("Opção inválida!")