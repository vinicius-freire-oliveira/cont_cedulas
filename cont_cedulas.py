# Solicita ao usuário o valor a ser sacado
numero = int(input('Valor para sacar: '))

# Conta quantas notas de R$200 são necessárias e atualiza o valor de "numero"
duzentos = int(numero / 200)
numero = numero - (duzentos * 200)

# Conta quantas notas de R$100 são necessárias e atualiza o valor de "numero"
cem = int(numero / 100)
numero = numero - (cem*100)

# Conta quantas notas de R$50 são necessárias e atualiza o valor de "numero"
cinquenta = int(numero/50)
numero = numero - (cinquenta*50)

# Conta quantas notas de R$20 são necessárias e atualiza o valor de "numero"
vinte = int(numero/20)
numero = numero - (vinte*20)

# Conta quantas notas de R$10 são necessárias e atualiza o valor de "numero"
dez = int(numero/10)
numero = numero - (dez*10)

# Conta quantas notas de R$5 são necessárias e atualiza o valor de "numero"
cinco = int(numero/5)
numero = numero - (cinco*5)

# Conta quantas notas de R$2 são necessárias e atualiza o valor de "numero"
dois = int(numero/2)
numero = numero - (dois*2)

# O restante, que sobrou após retirar as notas maiores, não pode ser retirado com as notas disponíveis
# Por isso, definimos a variável "restante" para armazenar o valor que não pode ser retirado
restante = numero

# Imprime o número de cada tipo de nota
print('Notas R$200,00 = ', duzentos)
print('Notas R$100,00 = ', cem)
print('Notas R$ 50,00 = ', cinquenta)
print('Notas R$ 20,00 = ', vinte)
print('Notas R$ 10,00 = ', dez)
print('Notas R$  5,00 = ', cinco)
print('Notas R$  2,00 = ', dois)

# Se houver algum valor que não possa ser retirado com as notas disponíveis, informa o usuário
if restante > 0:
    print(f'O valor restante de R${restante} não pode ser retirado com as notas disponíveis.')

