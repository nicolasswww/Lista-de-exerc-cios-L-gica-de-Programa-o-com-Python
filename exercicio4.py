# Exercício 4:
# Crie uma aplicação que gera uma folha de pagamento de um funcionário de uma concessionária.
# Esse software precisa mostrar na folha de pagamento o nome completo,
# CPF e outras 2 informações que ficará à critério do desenvolvedor.
# Antes da folha ser gerada, o usuário precisa informar também o salário base do funcionário,
# quantos automóveis ele vendeu no mês, o percentual ganho por comissão por automóveis vendido 
# (ex: cada automóvel vendido equivale à uma comissão de 10% do salário naquele mês), 
# além de outros benefícios (como vale-alimentação e vale-transporte). 
# No final esse software deve exibir todas essas informações da seguinte forma:
# ==========================
# INFORMAÇÃO EXTRA 1 | INFORMAÇÃO EXTRA 2
# ==========================
# SALÁRIO BASE DO FUNCIONÁRIO
# QUANTIDADE DE VEÍCULOS VENDIDOS NO MÊS
# PERCENTUAL DE COMISSÃO POR VEÍCULO VENDIDO (% EXTRA DO SALÁRIO)
# VALOR EM REAIS (R$) GANHO DE COMISSÃO
# VALOR EM REAIS (R$) GANHO DE VALE TRANSPORTE
# VALOR EM REAIS (R$) GANHO DE VALE ALIMENTAÇÃO
# VALOR EM REAIS (R$) TOTAL À RECEBER 

print("==========================")
nome = input("Digite o nome completo do funcionário: ")
cpf = input("Digite o CPF do funcionário: ")
idade = input("Digite a idade do funcionário: ")
cidade = input("Digite a cidade onde o funcionário mora: ")
salario_base = float(input("Digite o salário base do funcionário: "))
quantidade_veiculos = int(input("Digite a quantidade de automóveis vendidos no mês: "))
percentual_comissao = salario_base * 0.10
valor_comissao = percentual_comissao * quantidade_veiculos
vale_transporte = float(input("Digite o valor do vale-transporte: "))
vale_alimentacao = float(input("Digite o valor do vale-alimentação: "))
total_receber = salario_base + valor_comissao + vale_transporte + vale_alimentacao
print("==========================")
print(f"{nome} | {idade} anos")
print("==========================")
print(f"Salário Base: R$ {salario_base:.2f}")
print(f"Quantidade de Veículos Vendidos: {quantidade_veiculos}")
print(f"Percentual de Comissão: {percentual_comissao:.2f}%")
print(f"Valor da Comissão: R$ {valor_comissao:.2f}")
print(f"Vale Transporte: R$ {vale_transporte:.2f}")
print(f"Vale Alimentação: R$ {vale_alimentacao:.2f}")
print(f"Total à Receber: R$ {total_receber:.2f}")
