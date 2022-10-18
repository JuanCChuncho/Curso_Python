#print('Hola Mundo')
#Expresiones
#+,-, **,*,=,==,<,> >=,<=

radio_circulo=3
cadena_texto='Hola Mundo'

#tipos de datos
booleanos=True or False
entero=4 #int
decimales = 4.5 #float
cadena_texto='Hola Mundo' #str

print(type(decimales))


#print('Hola mundo'.center(60,'+')) # centrar la cadena de texto
#print('Hola mundo'.ljust(40,'+')) # justificar la cadena de texto hacia la izquierda
#print('Hola mundo'.rjust(40,'+')) # justificart la cadena de texto hacia la derecha
#print('hola mundo'.capitalize()) # Se haga mayusculas el primer caracter
#print('hola mundo'.upper())
#print('HOLA MUNDO'.lower())
#print('hola MUNDO'.swapcase())

primera_variable='programar en Python'
segunda_variable='didactico'
cadena_final=primera_variable+' '+segunda_variable
funcion_f=f'{primera_variable} {segunda_variable}'.upper().center(40,'=')
#print(len(funcion_f))
primero=primera_variable.replace('a','o')
#variable en una misma linea

nombre,apellido,edad,genero='Juan','Chuncho',34,'masculino'
print('El nombre del instructor es',nombre,apellido, 'y su edad ',edad,'de genero',genero)

primera_variable[0:5].find('u')


'r' in primera_variable
#print('Ingresar dato')
#ingresar_dato=int(input())
##print('Ingrese las cadenas')
##primera_cadena=input('Ingrese la primera cadena :' )
##segunda_cadena=input('Ingrese la segunda cadena :' )
##
##resultado=segunda_cadena[0:2]+primera_cadena[2:] +' '+primera_cadena[0:2]+segunda_cadena[2:]
##print('La cadena es:',resultado)


#costo='@el casta'
##costo+=' '
##costo+='es muy elevado'
##
##costo=input('')
##if 'a' in costo:
##    nueva_palabra=costo.replace('a','o')
##    print('La palabra corregida es: ',nueva_palabra)
##else:
##    print(False)

##print('Ingresar un primer valor')
##numero_entero=int(input())
##if numero_entero == 40:
##    print('El numero es igual al ingresado')
##elif numero_entero >= 20:
##    print('El numero es menor a 40')
##else:
##    print('Sigue intentando')


edad=int(input())
##if edad >=18:
##    print('Es mayor edad')
##elif edad >=15:
##    print('Es menor de edad')
##else:
##    print('Eres un niño')

if edad >18 or edad ==18:
    print('Eres mayor edad')
else:
    print('Intenta de nuevo')
    edad=int(input())
    if edad >18 or edad ==18:
        print('Eres mayor edad')
    

#bucle for

##for i in primera_variable:
##    print(i)
#for i in range(10):
#    print(i)
#for i in range(0,10,1):
#    print(i)
#taller
##for i in range(len(primera_variable)):
##    print(i)
##resultado=int(input())
##for i in range(1,13):
##    r=resultado*i
##    print(f'{resultado} x {i} =',r)

