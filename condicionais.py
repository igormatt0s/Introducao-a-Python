# Estruturas condicionais

idade = 20

if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')

"""
Imagine que você queira imprimir "Aprovado(o)", caso o estudande tenha uma média superior ou igual a 7, e "Reprovado", caso a média seja inferior a 7.
""" 
"""
media = float(input('Informe a média do estudante: '))

if media >= 7:
    print('Você foi Aprovado(a)!')
elif media >= 5: #else if (do contrário)
    print('Recuperação')
else:
    print('Você foi Reprovado(a).')
"""

media = 10
presenca = 100

if media >= 7 and presenca >= 70: #pode usar o and ou o or
    print('Aprovado(a')
    print('Parabéns!') # tudo o que estiver identado estará dentro da condição
else:
    print('Reprovado(a)')
    print('Tente novamente!')