import pandas as pd 

df = pd.DataFrame(
        [
            ['PE', 'Pernambuco', 'Recife'], ['RJ', 'Rio de Janeiro', 'Rio de Janeiro'],
            ['PB', 'Paraíba', 'João Pessoa'], ['SP', 'São Paulo', 'São Paulo'],
            ['MG', 'Minas Gerais', 'Belo Horizonte'], ['CE', 'Ceará', 'Fortaleza'],
            ['AC', 'Acre', 'Rio Branco'], ['MA', 'Maranhão', 'São Luís'], ['RN', 'Rio Grande do Norte', 'Natal'],
            ['PR', 'Paraná', 'Curitiba'], ['RS', 'Rio Grande do Sul', 'Porto Alegre']
        ], columns=['Sigla', 'Nome', 'Capital']
    )
   
print(df['Sigla'])

#Diz aonde começa, termina e o passo
print(df.index)
print()

#Diz a linha do indice que tu deseja, pode usar ix ou iloc
print(df.iloc[0])
print()

#Retornar o elementos do indice 0 até n-1 iloc[:n] 
print(df.iloc[:2])

















