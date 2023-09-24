'''
Exerrcicio 2- Lista 1 

 Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
 usando a seguinte fórmula: (72.7*altura) - 58

'''
#Solicita a altura da pessoa em cm
altura = float(input("Digite a sua altura em cm: "))

#Converte em Metros
alturaM = altura/100

#Utiliza a fórmula de peso ideal
PesoId = (72.7*alturaM)-58

#Arredonda o valor do peso para dois digitos após o "." do float
PesoID_arredondado = round(PesoId,2)

#Diz o peso ideal 
print(f"O seu peso ideal é de {PesoID_arredondado} kg")