#Importación de pandas
import pandas as pd
import csv

#Declaración de listas
fbk=['Facebook', 2449, True, 2006]
twt=['Twitter', 339, False, 2006]
ig=['Instagram', 1000, True, 2010]
yt=['Youtube', 2000, False, 2005]
lkn=['LinkedIn', 663, False, 2003]
wsp=['WhatsApp', 1600, True, 2009]

#Asignamos listas a una lista
lista_rrss=[fbk,twt,ig,yt,lkn,wsp]

#Construcción de dataframe
df_rrss=pd.DataFrame(
    lista_rrss,
    columns=['Name','Users','FBK property','Year']
)

#Impresión del dataframe creado
print(df_rrss)


#Guardado como un CSV
df_rrss.to_csv("c:/Users/monst/Desktop/Python/basicos/redes.csv")
 