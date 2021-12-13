import os
import msvcrt as m
import numpy as np

def limpiarConsola():
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"
    os.system(command)

def comprar_pasaje(vuelo,cum):
    cum = 0
    for i in vuelo:
        for j in i:
            print(j,end = "\t")
        print()
    print('\nAsientos Normales(1-30) = 78900\nAsientos VIP(31-42) = 240000')
    opciones=int(input('que pasaje desea comprar?: '))
    if opciones == 1:
        vuelo[0,0] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 2:
        vuelo[0,1] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 3:
        vuelo[0,2] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 4:
        vuelo[0,3] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 5:
        vuelo[0,4] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 6:
        vuelo[0,5] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 7:
        vuelo[1,0] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 8:
        vuelo[1,1] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 9:
        vuelo[1,2] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 10:
        vuelo[1,3] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 11:
        vuelo[1,4] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 12:
        vuelo[1,5] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 13:
        vuelo[2,0] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 14:
        vuelo[2,1] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 15:
        vuelo[2,2] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 16:
        vuelo[2,3] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 17:
        vuelo[2,4] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 18:
        vuelo[2,5] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 19:
        vuelo[3,0] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 20:
        vuelo[3,1] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 21:
        vuelo[3,2] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 22:
        vuelo[3,3] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 23:
        vuelo[3,4] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 24:
        vuelo[3,5] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 25:
        vuelo[4,0] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 26:
        vuelo[4,1] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 27:
        vuelo[4,2] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 28:
        vuelo[4,3] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 29:
        vuelo[4,4] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 30:
        vuelo[4,5] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 78900 * 0.85
        else:
            cum = 78900
    elif opciones == 31:
        vuelo[5,0] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 240000 * 0.85
        else:
            cum = 240000
    elif opciones == 32:
        vuelo[5,1] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 240000 * 0.85
        else:
            cum = 240000
    elif opciones == 33:
        vuelo[5,2] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 240000 * 0.85
        else:
            cum = 240000
    elif opciones == 34:
        vuelo[5,3] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 240000 * 0.85
        else:
            cum = 240000
    elif opciones == 35:
        vuelo[5,4] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 240000 * 0.85
        else:
            cum = 240000
    elif opciones == 36:
        vuelo[5,5] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 240000 * 0.85
        else:
            cum = 240000
    elif opciones == 37:
        vuelo[6,0] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 240000 * 0.85
        else:
            cum = 240000
    elif opciones == 38:
        vuelo[6,1] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 240000 * 0.85
        else:
            cum = 240000
    elif opciones == 39:
        vuelo[6,2] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 240000 * 0.85
        else:
            cum = 240000
    elif opciones == 40:
        vuelo[6,3] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 240000 * 0.85
        else:
            cum = 240000
    elif opciones == 41:
        vuelo[6,4] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 240000 * 0.85
        else:
            cum = 240000
    elif opciones == 42:
        vuelo[6,5] = 0
        run, nombre, fono, banco = datos()
        if banco == 'BancoDuoc':
            cum = 240000 * 0.85
        else:
            cum = 240000
    return vuelo, cum, opciones, run, nombre, fono, banco

def datos():
    opcion = 0
    run = input('Ingrese su RUT: ')
    nombre = input('Ingrese su Nombre: ')
    fono = input('Ingrese su Telefono: ')
    while opcion != 1 and opcion != 2 and opcion != 3:
        print('1. BancoEstado\n2. BancoSantander\n3. BancoDuoc')
        opcion = int(input('Seleccione su Banco: '))
        if opcion == 1:
            banco = 'BancoEstado'
        if opcion == 2:
            banco = 'BancoSantander'
        if opcion == 3:
            banco = 'BancoDuoc'
    return run, nombre, fono, banco

def anular_pasaje(v,opciones,vuelo):

        if opciones == 1:
            vuelo[0,0] = 1
            v.clear()
        elif opciones == 2:
            vuelo[0,1] = 2
            v.clear()
        elif opciones == 3:
            vuelo[0,2] = 3
            v.clear()
        elif opciones == 4:
            vuelo[0,3] = 4
            v.clear()
        elif opciones == 5:
            vuelo[0,4] = 5
            v.clear()
        elif opciones == 6:
            vuelo[0,5] = 6
            v.clear()
        elif opciones == 7:
            vuelo[1,0] = 7
            v.clear()
        elif opciones == 8:
            vuelo[1,1] = 8
            v.clear()
        elif opciones == 9:
            vuelo[1,2] = 9
            v.clear()
        elif opciones == 10:
            vuelo[1,3] = 10
            v.clear()
        elif opciones == 11:
            vuelo[1,4] = 11
            v.clear()
        elif opciones == 12:
            vuelo[1,5] = 12
            v.clear()
        elif opciones == 13:
            vuelo[2,0] = 13
            v.clear()
        elif opciones == 14:
            vuelo[2,1] = 14
            v.clear()
        elif opciones == 15:
            vuelo[2,2] = 15
            v.clear()
        elif opciones == 16:
            vuelo[2,3] = 16
            v.clear()
        elif opciones == 17:
            vuelo[2,4] = 17
            v.clear()
        elif opciones == 18:
            vuelo[2,5] = 18
            v.clear()
        elif opciones == 19:
            vuelo[3,0] = 19
            v.clear()
        elif opciones == 20:
            vuelo[3,1] = 20
            v.clear()
        elif opciones == 21:
            vuelo[3,2] = 21
            v.clear()
        elif opciones == 22:
            vuelo[3,3] = 22
            v.clear()
        elif opciones == 23:
            vuelo[3,4] = 23
            v.clear()
        elif opciones == 24:
            vuelo[3,5] = 24
            v.clear()
        elif opciones == 25:
            vuelo[4,0] = 25
            v.clear()
        elif opciones == 26:
            vuelo[4,1] = 26
            v.clear()
        elif opciones == 27:
            vuelo[4,2] = 27
            v.clear()
        elif opciones == 28:
            vuelo[4,3] = 28
            v.clear()
        elif opciones == 29:
            vuelo[4,4] = 29
            v.clear()
        elif opciones == 30:
            vuelo[4,5] = 30
            v.clear()
        elif opciones == 31:
            vuelo[5,0] = 31
            v.clear()
        elif opciones == 32:
            vuelo[5,1] = 32
            v.clear()
        elif opciones == 33:
            vuelo[5,2] = 33
            v.clear()
        elif opciones == 34:
            vuelo[5,3] = 34
            v.clear()
        elif opciones == 35:
            vuelo[5,4] = 35
            v.clear()
        elif opciones == 36:
            vuelo[5,5] = 36
            v.clear()
        elif opciones == 37:
            vuelo[6,0] = 37
            v.clear()
        elif opciones == 38:
            vuelo[6,1] = 38
            v.clear()
        elif opciones == 39:
            vuelo[6,2] = 39
            v.clear()
        elif opciones == 40:
            vuelo[6,3] = 40
            v.clear()
        elif opciones == 41:
            vuelo[6,4] = 41
            v.clear()
        elif opciones == 42:
            vuelo[6,5] = 42
            v.clear()
        return v, vuelo
        

def modificar_pasaje(v):
    opcion = 0
    yapo = 0
    while (yapo !=5):
        print("Desea modificar algun dato? \n 1-Banco\n 2-Run\n 3-Nombre\n 4-fono\n 5-No deseo modificar ninguno de mis datos\n")
        yapo = int(input('Que opcion desea elegir?: '))
        if yapo == 1:
            print('Bancos Disponibles\n')
            print('1. BancoEstado\n2. BancoSantander\n3. BancoDuoc')
            while opcion != 1 and opcion != 2 and opcion != 3:
                opcion = int(input('Seleccione su Banco: '))
                if opcion == 1:
                    v['Banco'] = 'BancoEstado'
                if opcion == 2:
                    v['Banco'] = 'BancoSantander'
                if opcion == 3:
                    v['Banco'] = 'BancoDuoc'
            return v
        if yapo == 2:
            print('\nRut Actual ' + v['Rut'])
            v['Rut'] = input('\nCual sera su nuevo Run?: ')
            return v
        if yapo == 3:
            print('\nSu nombre actual ' + v['Nombre'])
            v['Nombre'] = input('\nCual sera su nuevo Nombre?: ')
            return v
        if yapo == 4:
            print('\nSu fono actual sera' + v['fono'])
            v['Telefono'] = input('\nCual sera su nuevo fono?: ')
            return v
