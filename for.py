for var in range(10): #para var dentro do range (faixa) 10 faça tal coisa:
    print(var)

for var in range(1, 10): #para var dentro do range (faixa) 10 faça tal coisa:
    print(var)

for var in range(1, 10, 2): #para var dentro do range (faixa) 10 faça tal coisa:
    print(var)

soma = 0

for i in range(1, 4):
    nota = float(input((f'Informe a sua nota {i}: '))) # {i} é o f-string

    soma = soma + nota

print(soma/3)