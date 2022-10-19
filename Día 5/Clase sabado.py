import pandas as pd
import numpy as np
import os
import pylab as plt

data=pd.read_excel('da.xlsx',skiprows=0)
x=data['Ingresos']
print(len(x))
lista_nueva=list(x)
print(len(lista_nueva))

x2=(data['Cantidad de ingresos'])
print(len(x2))
ingresos=[]
cantidad_ingresos=[]
totalingresos=[]

egresos=[]
cantidad_egresos=[]
totalegresos=[]

y=data['Cantidad de egresos']
y2=data['Egresos']


for i in range(0,len(x)):
    c=ingresos.append(x[i])
    c1=cantidad_ingresos.append(x2[i])
    c3=x[i]*x2[i]
    totalingresos.append(c3)
    e=egresos.append(y2[i])
    e2=cantidad_egresos.append(y[i])
    #e3=y2[i]*y[i]
    totalegresos.append(y2[i]*y[i])

tabla={'Total de ingresos':totalingresos,
       'Total de egresos':totalegresos}
df=pd.DataFrame(tabla)
suma_total=df['Total de ingresos'].sum()
writer = pd.ExcelWriter('Resultados.xlsx')
df.to_excel(writer,'Mi primera hoja',index=True)
writer.save()
