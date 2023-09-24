
'''
Exercicio 1 - Lista 1 
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo .
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo

'''
# Solicita os numeros inteiros
numero1 = int(input("Digite o primeiro número :"))
numero2 = int(input("Digite o Segundo Número:"))

# Solicita o numero real
numero3 = float(input("Digite um número real:"))

# Calcula o produto do dobro do primeiro com a metade do segundo
results1 = (2*numero1)*(numero2/2)

# Calcula a soma do triplo do primeiro com o terceiro
results2 = ((3)*numero1)+(numero3)

# Calcula o terceiro elevado ao cubo
results3 = numero3**3

# Exibe o resultado
print(f'O produto do dobro do primeiro com a metade do segundo é de {results1}')
print(f'A soma do triplo do primeiro com o terceiro é de : {results2} ')
print(f'O cubo do terceiro número é igual à : {results3}')
