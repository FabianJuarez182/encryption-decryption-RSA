# Universidad del Valle de Guatemala
# Departamento de Ingeniería
# Matematica Discreta seccion 10
# Fabián Estuardo Juárez Tello 21440
# Catedrático: Mario Castillo

diccionario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
listaCasteada = list()
listaLlave = list()
key = ''
M = ''
C = ''
p = 0
q = 0
n = 0
e = 0
ro = 0

#Metodo que permite el ingreso de los datos para encriptar el mensaje
def ingreso_encriptacion():
    global M
    M = input('Ingrese el mensaje a encriptar: ')
    global key
    key = input ('Ingrese la llave publica ejemplo:(e,n) con parentesis y coma:  ')
    keyreplace = key.replace('(', '')
    keyreplace = keyreplace.replace(')','')
    keysplit = keyreplace.split(',')
    global e
    e = int(keysplit[0])
    global n
    n = int(keysplit[1])
    print('Ya ha ingresado todos los datos a utilizar para encriptar el mensaje')
    print("Empezando a encriptar")

#Metodo que permite el ingreso de los datos para desencriptar el mensaje
def ingreso_desencriptacion():
    global C
    C = input('Ingrese el mensaje a desencriptar: ')
    global p
    p = int(input('Ingrese el valor de p: '))
    global q
    q = int(input('Ingrese el valor de q: '))
    global e
    e = int(input('Ingrese el valor de e: '))
    global n
    n = p*q
    global ro 
    ro = (p-1)*(q-1)
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
        if(resultado < 10):
            parseo = "0" + str(resultado)
            listaCasteada.append(parseo)
        else:
            parseo = str(resultado)
            listaCasteada.append(parseo)
    numBloques = str(len(diccionario)-1)
    bandera = False
    caracteres = 1
    while bandera == False:
        if int(numBloques) > n:
            bandera = True
            caracteres = caracteres - 1
        else:
            caracteres = caracteres + 1
            numBloques = numBloques + str(len(diccionario))
    encriptarParte1 = ''
    encriptarParte2 = ''
    for i in range(caracteres):
            encriptarParte1 = encriptarParte1 + listaCasteada[i]
            encriptarParte2 = encriptarParte2 + listaCasteada[i+2]
    numfinalbloque1 = int(encriptarParte1)**e % n
    numfinalbloque2 = int(encriptarParte2)**e % n
    print ('bloque 1 :',numfinalbloque1)
    print ('bloque 2 :',numfinalbloque2)
    print('\nMensaje encriptado: ',numfinalbloque1, "", numfinalbloque2)





#Metodo que realizara la Desencriptacion RSA
def accion2():
    print('\nHas elegido desencriptacion')
    ingreso_desencriptacion()

    for d in range(1,ro):
        if((e%ro)*(d%ro) % ro==1):
            D = d
    Csplit = C.split(' ')
    Bloque1 = int(Csplit[0])
    Bloque2 = int(Csplit[1])
    P1 = Bloque1**D %n
    P2 = Bloque2**D %n

    if(P1<1000):
        P1str = '0' + str (P1)
    else:
        P1str = str (P1)
    if(P2<1000):
        P2str = '0' + str (P2)
    else:
        P2str = str (P2)
    l1 = P1str[0] + P1str[1]
    l2 = P1str[2] + P1str[3]
    l3 = P2str[0] + P2str[1]
    l4 = P2str[2] + P2str[3]
    MensajeDesencriptado = diccionario[int(l1)]+ diccionario[int(l2)] + diccionario[int(l3)] + diccionario[int(l4)]
    print('\nMensaje desencriptado: ',MensajeDesencriptado)


#Metodo que cerrara el programa si el usuario lo elije
def salir():
    print('Saliendo')
    exit()

if __name__ == '__main__':
    menu_principal()