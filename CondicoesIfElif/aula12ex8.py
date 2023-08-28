# Exercício 43
# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule e mostre seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18,5: Abaixo do peso
# - Entre 18,5 e 25: Peso ideal
# - Entre 25 e 30: Sobrepeso
# - Entre 30 e 40: Obesidade
# - Acima de 40: Obesidade mórbida

peso = float(input('Peso em quilos: '))
altura = float(input('Altura em metros: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Seu IMC é {:.2f}, logo você está abaixo do peso.'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é {:.2f}, logo você está no peso ideal.'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu IMC é {:.2f}, logo você está em sobrepeso.'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu IMC é {:.2f}, logo você está em obesidade.'.format(imc))
else:
    print('Seu IMC é {:.2f}, logo você está em obesidade mórbida.'.format(imc))
