'''
Exercicio 4 - Lista 1
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de 
São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas.
'''
# Entrada do peso do peixe
peso = float(input("Digite o peso do peixe :"))

# Peso Limite
peso_limite = 50.0

# Verifica se o peso é maior que o peso imposto pela legislação
if peso > peso_limite:

    # Calcula o excedente
    excedente = peso-peso_limite

    # Arredonda o valor do excedente para deixar com dois dígitos
    excedenteAr = round(excedente, 2)

    # Calcula a multa de acordo com o valor do excedente
    multa = excedenteAr*4

    # Mostra os resultados obtidos
    print(f"O peso do peixe passou do limite em {excedenteAr}kg")
    print(f"A multa a ser paga é de: R${multa}")
else:
    # Caso o peso do peixe esteja dentro dos padrões, o programa informa através do print
    print("Nenhuma multa será aplicada. O peixe se encontra nos padrões de insenção dentro do estado de São Paulo")
