casa = int(input('Digite o valor do imóvel: '))
prestacao = int(input('Em quantos anos você deseja pagar: '))
salario = int(input('Digite seu salário: '))
meses = prestacao * 12
salario_att = salario*30/100
valor_att = casa / meses

if salario_att >= valor_att:
    print('Crédito aprovado')
else:
    print('Crédito reprovado')
print("====================================================================")
print (f'Em {meses} meses você precisará pagar, ao menos, {valor_att} por mês')