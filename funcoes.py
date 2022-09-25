# Criação de Funções

# Função inicial

def saudacao():
    print('Seja bem vindo(a)')# os comandos da função vão estar dentro da identação
    print('Olá!\n É um prazer ter você fazendo parte desse curso!')

saudacao()
saudacao()
saudacao()

#Função com parâmetros

def saudacao(nome, curso): # recebe um parâmetro nome e curso
    print(f'Seja bem vindo(a), {nome}')
    print(f'Olá!\n É um prazer ter você fazendo parte do curso de {curso}!')

saudacao('Igor', 'Python') # você deve passar os dois valores
saudacao('Mattos', 'HTML')

# Função com parâmetros default

def saudacao(nome, curso = 'Python'): # recebe um parâmetro nome
    print(f'Seja bem vindo(a), {nome}')
    print(f'Olá!\n É um prazer ter você fazendo parte do curso de {curso}!')

saudacao('Igor',)
saudacao('Igor', 'HTML') # O valor assumido por curso vai ser HTML

# Funções com retorno

def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)

print('O resultado da soma é', resultado)

def calculadora(num1, num2, operacao = '+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    
resultado = calculadora(10, 20)
print(resultado)

resultado = calculadora(10, 20, '-')
print(resultado)