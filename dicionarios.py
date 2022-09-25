# Criando dicionários

dicionario = {} # Dicionário vazio
dicionario = dict() # Dicionário vazio também

dicionario = {'nome': 'Igor', 'idade': 21, 'altura': 1.77}

print(dicionario)
print(dicionario['idade']) # acessar o valor da label idade

# Adicionando elementos em um dicionário

dicionario['programador'] = True

print(dicionario)

dicionario['altura'] = 2 # sobrescrever o conteúdo da chave

print(dicionario)

# Iterando sobre um dicionário, ou seja, percorrer soobre as chaves de um dicionário

for var in dicionario:
    print(var) # ele vai percorrer as chaves do dicionario
    print(dicionario[var]) # ele vai percorrer os valores do dicionario

# Testando a existência de uma chave em um dicionário

print('peso' in dicionario) # ele vai retornar False porque a chave 'peso' não está dentro do dicionario

print('altura' in dicionario) # ele vai retornar True porque a chave 'altura' existe dentro do dicionario