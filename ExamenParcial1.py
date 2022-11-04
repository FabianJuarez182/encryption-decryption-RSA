# Universidad del Valle de Guatemala
# Departamento de Ingeniería
# Matematica Discreta seccion 10
# Fabián Estuardo Juárez Tello 21440
# Catedrático: Mario Castillo

diccionario = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
listaCasteada = list()
M = ''
p = 0
q = 0

#Metodo que permite el ingreso de los datos para encriptar el mensaje
def ingreso_encriptacion():
    global M
    M = input('Ingrese el mensaje a encriptar: ');
    p = int(input('Ingrese el valor de p: '))
    q = int(input('Ingrese el valor de q: '))
    e = int(input('Ingrese el valor de e: '))
    n = p*q
    ro = (p-1)*(q-1)
    print("Su valor de n es:",n)
    print("Su valor de ro es:",ro)
    print('Ya ha ingresado todos los datos a utilizar para encriptar el mensaje')
    print("Empezando a encriptar")

#Metodo que permite el ingreso de los datos para desencriptar el mensaje
def ingreso_desencriptacion():
    C = input('Ingrese el mensaje a encriptado: ')
    n = int(input('Ingrese el valor de n de la llave publica: '))
    e = int(input('Ingrese el valor de e de la llave publica: '))
    print('Ya ha ingresado todos los datos a utilizar para desencriptar el mensaje')
    print("Empezando a desencriptar")

#Metodo que posee la creacion del menu y su muestra
def mostrar_menu(opciones):
    print('\nSeleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

#Metodo que leera la opcion ingresada por el usuario y devolvera error si no ha escogido una valida
def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

#Metodo que ejecutara la opcion escogida por el usuario
def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

#Metodo que genera el menu en base a las opciones y las salidas que hay a mostrar
def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

#Metodo que se utilizara para llevar a cabo todos los procesos (sera el metodo main)
def menu_principal():
    opciones = {
        '1': ('Encriptacion', accion1),
        '2': ('Desencriptacion', accion2),
        '3': ('Salir',salir)
    }
    generar_menu(opciones, '3')

#Metodo que realizara la Encriptacion
def accion1():
    print('\nHas elegido la encriptacion')
    ingreso_encriptacion()
    longCadena = len(M)
    for i in range(longCadena):
        resultado = diccionario.index(M[i])
        print(resultado)
        if(resultado < 10):
            parseo = "0" + str(resultado)
            print(parseo)
            listaCasteada.append(parseo)
        else:
            listaCasteada.append(parseo)
    print(listaCasteada)


#Metodo que realizara la Desencriptacion RSA
def accion2():
    print('\nHas elegido desencriptacion')
    ingreso_desencriptacion()



#Metodo que cerrara el programa si el usuario lo elije
def salir():
    print('Saliendo')
    exit()

if __name__ == '__main__':
    menu_principal()