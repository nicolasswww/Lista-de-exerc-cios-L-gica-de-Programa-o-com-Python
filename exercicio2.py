# Crie uma aplicação que recebe o nome, a turma, a matéria desejada e as notas do estudante.
# ENQUANTO o usuário não finalizar a inserção de novas notas, ele somará elas.
# Caso ele não queira mais passar nenhuma nova nota,
# o código deve dividir a soma pela quantidade de notas.
# O código deve informar se o aluno passou, reprovou ou se está em exame. 
# Dica do prof Bruno
# Primeiro criem variáveis e depois pensem no que vocês precisam fazer

print("Sistema de notas acadêmicas.")
nome = str(input("Digite o nome do aluno: "));
turma = int(input("Diga qual a sua turma: "));
materia = str(input("Digite o nome da matéria: "));
nota = int(input("Digite a primeira nota: "))
notaNova = 0.0;
somaNota = 0.0;
opcao = 1
divisaoDaNota = 0.0;
qtdNota = 0.0;

while opcao == 1:
    print("Deseja adicionar mais notas?\n1 - Sim\n0 - Não")
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        notaNova = int(input("Digite a nota nova: "))
        somaNota = nota + notaNova
        
    elif opcao == 0:
        divisaoDaNota = somaNota / notaNova 
        print(nome, ", a sua média é: ", divisaoDaNota)

        
       
        
    

