
# Crie uma aplicação que recebe o nome, a turma, a matéria desejada e as notas do estudante.
# ENQUANTO o usuário não finalizar a inserção de novas notas, ele somará elas.
# Caso ele não queira mais passar nenhuma nova nota,
# o código deve dividir a soma pela quantidade de notas.
# O código deve informar se o aluno passou, reprovou ou se está em exame. 
# Dica do prof Bruno
# Primeiro criem variáveis e depois pensem no que vocês precisam fazer

print("Sistema de notas acadêmicas.")
nome = str(input("Digite o nome do aluno: "))
turma = int(input("Diga qual a sua turma: "))
materia = str(input("Digite o nome da matéria: "))
nota = float(input("Digite a primeira nota: "))
somaNota = nota
qtdNota = 1
opcao = 1

while opcao == 1:
    print("Deseja adicionar mais notas?\n1 - Sim\n0 - Não")
    opcao = int(input("Digite a opção: "))
    
    if opcao == 1:
        notaNova = float(input("Digite a nota nova: "))
        somaNota += notaNova
        qtdNota += 1
    elif opcao == 0:
        if qtdNota > 0:
            media = somaNota / qtdNota
            print(nome," a sua média é: ", media)
        else:
            print("Nenhuma nota foi inserida.")

        
       
        
    

    
