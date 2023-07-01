import os
import sys

#funcion para leer el archivo
def leer_archivo():
    array = list()
    nombre_archivo = "Diccionario.txt"  
    archivo = open(nombre_archivo, "r")
    for line in archivo:
        array.append(line)  
    archivo.close()
    return array



#funcion para organizar la lista por orden alfabetico
def orden_alfabetico():
    contenido = leer_archivo()
    # Crear una lista principal con 26 elementos(cantidad de numeros exactos que hay en el alfabeto)
    lista_principal = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    for cont in contenido:
        letra = ord(cont[0])
        if letra >= 65 and letra <= 90:
            lista_principal[letra-65].append(cont)
        if letra >= 97 and letra <= 122:
            lista_principal[letra-97].append(cont)
    return lista_principal

#funcion para imprimir por orden alfabetico
def imprimir_diccionario(result):
    for imprimir in result:
        if imprimir is not None:
            for i in imprimir:
                if i is not None:
                    print("\n",i)
                


#funcion para buscar las palabras a partir de su letra
def buscar_palabra(recibir):
    print("ingrese una letra:" )
    letra = sys.stdin.read(1)
    os.system('cls')
    print("la letra que ingreso fue: ",letra )
    codigo = ord(letra)
    if codigo >= 65 and codigo <= 90:
        codigo = codigo-65  
    if codigo >= 97 and codigo <= 122:
        codigo = codigo-97
    if recibir[codigo] is not None:
        vandera = 0
        indice = recibir[codigo]
        for i in indice:
                if i is not None:
                    print("\n",i)
                    vandera = 1
            
        if vandera == 0 :
           print("\nno tenemos informacion de esa letra en nuestro diccionario, disculpe") 
    input("\npresione enter para continuar...")


    
         
     
result = orden_alfabetico()
imprimir_diccionario(result)
buscar_palabra(result)
     
        
        
        



