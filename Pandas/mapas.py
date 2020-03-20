import matplotlib.pyplot as plt
import pandas as pd
import mplleaflet

df = pd.read_csv('copacabana_lat_lng.csv')
print(df.head())

#Plotando a latitude e longitude dos imóveis
plt.scatter(df['lng'],df['lat'],marker = '.')
mplleaflet.show()




