valorTotal = 0.0
valorNovoProduto = 0.0
opcao = 1


nome = str(input("Digite o nome do cliente: "));

while opcao == 1:
    print("O que você deseja?\n1 - Adicionar produto\n0 - Finalizar compra")
    opcao = int(input("Digite a opção: "))
    
    if opcao == 1:
        valorNovoProduto = float(input("Valor de produto: R$"))
        valorTotal = valorTotal + valorNovoProduto
        
    elif opcao == 0:
        print(nome, "você deve pagar R$", valorTotal)



