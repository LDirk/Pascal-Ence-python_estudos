import pandas as pd 
#Banco de dados de teste 
from db import DemoDB

database = DemoDB()

#Verifica as tabelas do demodb
print(database.tables)
print()


#Pegando o database album
album = database.tables.Album.all()
print(album.head())
print()

#Pegando o artista
artist = database.tables.Artist.all()
print(artist.head())
print()
print() 

#Juntando album e artistas
album_artist = pd.merge(artist, album)
print(album_artist.head())
print()

#Renomeando as colunas , inplace é para ir direto ao data frame
album.rename(columns = {'ArtistId': "Artist_ID"}, inplace = True)
print(album.head())


alunos1 = pd.DataFrame(
	{
		'nome':['Maria','Sofia'],
		'nota':[8,9]
	}
)

alunos2 = pd.DataFrame(
	{
		'nome':['Joao','Pedro', 'Maria'],
		'cod':[1,2,3]
	}
)
print()
#Pegando tudo em vez de so a interseção
alunos_total = pd.merge(alunos1, alunos2, how = "outer")
print(alunos_total.head())

