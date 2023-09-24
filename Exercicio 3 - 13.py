'''
Exercicio 3 - Lista 1

Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
a)Para homens: (72.7*h) - 58
b)Para mulheres: (62.1*h) - 44.7
'''
#Entrada de dados
sexo = str(input("Digite o seu sexo [M/F], sendo M para masculino e F para feminino: "))
altura = float(input('Digite sua altura em centímetros:'))
#Converte altura de cm para metros
alturaM=altura/100
#Verifica se a string que entrou foi M
if sexo.upper() =="M":
    PesoM=(72.7*alturaM)-58
    #limita o peso a dois dígitos após o "."
    PesoMar=round(PesoM,2)
    #Exibe o resultado
    print(f'O seu peso ideal é de:{PesoMar}kg')
elif sexo.upper()=='F':
    PesoF=(62.1*alturaM)-44.7
    PesoFar = round(PesoF,2)
    #Mostra o resultado
    print(f"O seu peso ideal é de : {PesoFar}kg")
else:
    print ("Sexo desconhecido. Por favor, Digite M para masculino ou F para Feminino.")
    