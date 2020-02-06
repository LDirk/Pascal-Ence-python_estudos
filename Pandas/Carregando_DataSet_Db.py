from db import DB 

#Arquivo no mesmo diretorio
database = DB(filename = "logs.sqlite3", dbtype = 'sqlite')
#Mostra as tabelas
print(database.tables)
print()

#visualizar data_frame
log_df = database.tables.log.all()
print(log_df)

