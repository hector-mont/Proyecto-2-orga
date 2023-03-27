import csv
from Juego import Juego

#Leer y escribir

def cargar_juego(juegos):
    with open('juegos.csv','r') as archivo_csv:
        csv_lector = csv.reader(archivo_csv)

        for line in csv_lector:
            juego = Juego(
                modelo=line[0],
                titulo=line[1],
                precio=line[2],
                status=line[3]
            )
            juegos.append(juego)

    return juegos





def main():
    # Inicializacion
    juegos = []


    while True:
        seleccion = input('''Por favor, seleccione una opción:
        1. Registro.
        2. Busqueda.
        3. Alquiler.
        4. Devolución.
        5. Eliminar. 
        6. Salir.
        >> ''')
        while (not seleccion.isnumeric()) or (int(seleccion) not in range(1,7)):
            seleccion = input('Por favor, ingrese una opción válida: ')

        if seleccion == '1':
            #bla bla bla
        elif seleccion == '2':
            #bla bla
        elif seleccion == '3':
            #bla bla bla
        elif seleccion == '4':
            #,fld
        elif seleccion == '5':
            #dns
        else:
            print('Hasta luego')
            break