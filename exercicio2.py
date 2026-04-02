
# Crie uma aplicação que recebe o nome, a turma, a matéria desejada e as notas do estudante.
# ENQUANTO o usuário não finalizar a inserção de novas notas, ele somará elas.
# Caso ele não queira mais passar nenhuma nova nota,
# o código deve dividir a soma pela quantidade de notas.
# O código deve informar se o aluno passou, reprovou ou se está em exame. 
# Dica do prof Bruno
# Primeiro criem variáveis e depois pensem no que vocês precisam fazer

print("Sistema de notas acadêmicas.")
nome = str(input("Digite o nome do aluno: "))
turma = str(input("Diga qual a sua turma: "))
materia = str(input("Digite o nome da matéria: "))
nota = 0.0
qtd_notas = 0
opcao_tela = 1

while opcao_tela == 1:
    opcao_tela = int(input("O que você deseja?\n[1] - Adicionar nota\n[0] - Sair\nOpção: "))
    if opcao_tela == 1:
        qtd_notas += 1

        nova_nota = float(input(qtd_notas, "ª nota do estudante: "))
        nota = nota + nova_nota
        
    else:
        media = nota / qtd_notas
        print("Média do estudante: ", media)

    if media >= 6:
        print("Você passou!")

    elif media <= 5:
        print("Você reprovou!")


