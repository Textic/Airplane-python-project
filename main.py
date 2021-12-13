import funciones as fn
import numpy as np
selection = 0
vuelo=[]
vuelo = np.array([
    [1,2,3,4,5,6],
    [7,8,9,10,11,12],
    [13,14,15,16,17,18],
    [19,20,21,22,23,24],
    [25,26,27,28,29,30],
    [31,32,33,34,35,36],
    [37,38,39,40,41,42],])
cum = 0
asiento = {}

while(selection != 5):
    fn.limpiarConsola()
    print("Menu")
    print("1. Ver pasajes disponibles")
    print("2. Comprar pasaje")
    print("3. Anular vuelo")
    print("4. Modificar datos de pasajero")
    print("5. Salir")
    selection = int(input("\nElije una opcion: "))
    
    if selection == 1: #Ver pasajes disponibles
        fn.limpiarConsola()
        for i in vuelo:
            for j in i:
                print(j,end = "\t")
            print()
        input("\nPresione la tecla enter para volver al menu anterior...")
    if selection == 2: #Comprar pasajes
        fn.limpiarConsola()
        vuelo, cum, opciones, run, nombre, fono, banco  = fn.comprar_pasaje(vuelo, cum)
        asiento[opciones] = {
            "Rut":run,
            "Nombre":nombre,
            "Telefono":fono, 
            "Banco":banco,
            "Paga":cum}
    if selection == 3: #Anular pasajes
        fn.limpiarConsola()
        for i in vuelo:
            for j in i:
                print(j,end = "\t")
            print()
        opciones = int(input('\nQue pasaje desea anular?: '))
        v = asiento[opciones]
        asiento[opciones], vuelo = fn.anular_pasaje(v, opciones, vuelo)
    if selection == 4: #Modificar pasajes
        fn.limpiarConsola()
        for i in vuelo:
            for j in i:
                print(j,end = "\t")
            print()
        opciones = int(input('\nQue pasaje desea modificar?: '))
        v = asiento[opciones]
        asiento[opciones] = fn.modificar_pasaje(v)
    if selection == 5: #Salir
        print('Saliendo del programa\n\n')

