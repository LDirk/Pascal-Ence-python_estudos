import pandas as pd

#data frame é praticamente uma matriz
#Colummns você nomeia as colunas

df = pd.DataFrame([["fchollet/keras", 11302],["Openai/universe", 4350],["Pandas-dev/pandas",8168]],
	columns = ["Repositoty", 'Stars'])

#shape diz a dimensão da matriz
print(df.shape)
print()
print(df)
print()

#Verificar uma coluna, df['nome_coluna']
print(df['Stars'])
print()

#Média das estrelas
print(df['Stars'].mean())
print()

#Mediana
print(df['Stars'].median())

#Acessando uma linha especifica , iloc[linha que tu quer]
print(df.iloc[1])

