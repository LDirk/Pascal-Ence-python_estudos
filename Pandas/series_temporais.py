import pandas as pd 
from db import DB   

database = DB(filename = 'logs.sqlite3', dbtype = 'sqlite')

log_df = database.tables.log.all()
print(log_df.head())
print()

#Convertendo date em data
log_df['date'] = pd.to_datetime(log_df['date'], format = '%Y-%m-%d %H:%M:%S.%f')
print(log_df.dtypes)
print()
print()

#Colocando date como indice para fazer filtros 
log_df.set_index(['date'], inplace = True)
print(log_df.head())
#Agora fazer o filtro na data 
print(log_df['2017'])
print(log_df['2017-01-03'])
print(log_df['2017-01-03 10:47': '2017-01-03 10:51'])