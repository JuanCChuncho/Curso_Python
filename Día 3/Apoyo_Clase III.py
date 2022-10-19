
miprimera_lista=['Loja','Cuenca','Quito','Guayaquil']
miprimera_lista.insert(1,'Ambato')
segunda_lista=['Esmeraldas',2]
lista_final=miprimera_lista+segunda_lista
lista_nu=[2,5,1,7]
lista_nu[0]=3
mi_primer_diccionario={'Nombres':'Juan','Apellidos':'Chuncho'}
mi_primer_diccionario['Nombres']
mi_primer_diccionario.keys()
mi_primer_diccionario.values()
mi_primer_diccionario.items()

mi_primer_diccionario['Edad']=34
mi_primer_diccionario.update({'dicta materias':['M',50]})
mi_primer_diccionario.pop('Edad')

tupla=('hola','Mundo')
lista=list(tupla)




list_vacia=[]
for i in miprimera_lista:
    list_vacia.append(i)

nombres = ["Juan", "Fernando", "Jack", "Jessica", "Guillermo"]
info = []
for n in nombres:
    apell = input("¿Cual es el apellido de " + n + "?")
    info.append(apell)
