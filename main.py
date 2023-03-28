import csv
from Juego import Juego

#Leer y escribir

def cargar_juegos(juegos):
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

def guardar_juegos(juegos):
    with open('juegos.csv','w') as archivo_csv:
        csv_escritor = csv.writer(archivo_csv)

        for juego in juegos:
            line = [
                juego.modelo,
                juego.titulo,
                juego.precio,
                juego.status
            ]
            csv_escritor.writerow(line)





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
    def menu(self):
        self.cargar_datos()
        while True:
            print("""\n------- Bienvenido a Rent A Game ------- \n
            1. Inserción de un nuevo juego.
            2. Búsqueda de juego por modelo.
            3. Búsqueda de juego por título.
            4. Alquiler de un juego.
            5. Devolución de un juego.
            6. Eliminacion de un juego.
            7. Salir
            """)

            while True:
                try:
                    option = int(input('\nIngrese una opción: '))
                except ValueError:
                    print("Debes escribir un número.")
                    continue
                else:
                    break

            if option == 1:
                self.insertar_juego()
            elif option == 2:
                self.buscar_por_modelo()   
            elif option == 3:
                self.buscar_por_titulo()         
            elif option == 4:
                self.alquilar_juego()
            elif option == 5:
                self.devolver_juego()
            elif option == 6:
                self.eliminar_juego()
            elif option == 7:
                self.guardar_datos()
                break
            else:
                print('Opción inválida')
