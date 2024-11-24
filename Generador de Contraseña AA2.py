"""
Juego Programación (Generar contraseña segura)
"""
#variables y librerias
import random
LETRAS = "abcdefghijklmñnopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
SIMBOLOS = "!#$%&'()*+,-./:;<=>?@[]^_`{|}~"
NUMEROS = "0123456789"
#menu inicio
print ("BIENVENIDO AL GENERADOR DE CONTRASEÑAS MÁS SEGURO")
TEXTO = """Opciones:
1. Solo con letras (mayúsculas y minúsculas)
2. Solo con símbolos
3. Con mayúsculas, minúsculas y símbolos
"""
print (TEXTO)
#ingresar opcion de menu
OPCIONMENU = int(input("Ingresa el número de la opción:\n"))
if OPCIONMENU == 1 :
    #caso 1
        #largo contraseña
    LARGO = int(input("¿De cuántos caracteres deseas la contraseña?:\n"))
        #sacar caracteres al azar de "LETRAS" definiendo la cantidad de caracteres "LARGO"
    SORTEO1= random.sample(LETRAS,LARGO)
        # aqui lo escribiría así: [A], [B], [C] ...
        # para unirlo:
    CONTRASENAGENERADA1 = "".join(SORTEO1)
    #imprimir contraseña al usuario
    print("Su contraseña generada es:\n", CONTRASENAGENERADA1)
    print("Gracias por usar este programa")
elif OPCIONMENU == 2:
    #caso 2
        #largo contraseña
    LARGO = int(input("¿De cuántos caracteres deseas la contraseña?:\n"))
        #sacar caracteres al azar de "LETRAS" definiendo la cantidad de caracteres "LARGO"
    SORTEO2= random.sample(SIMBOLOS,LARGO)
        # aqui lo escribiría así: [}], [.], [+] ...
        # para unirlo:
    CONTRASENAGENERADA2 = "".join(SORTEO2)
    #imprimir contraseña al usuario
    print("Su contraseña generada es:\n", CONTRASENAGENERADA2)
    print("Gracias por usar este programa")

elif OPCIONMENU == 3:
    #escoger la cantidad de letras, numeros y simbolos
    CANTIDADLETRAS3 = int(input("¿Cuántas letras deseas en la contraseña?:\n"))
    CANTIDADNUMEROS3 = int(input("¿Cuántos números deseas en la contraseña?:\n"))
    CANTIDADSIMBOLOS3 = int(input("¿Cuántos símbolos deseas en la contraseña?:\n"))

    LETRASRANDOM3 = random.sample(LETRAS,CANTIDADLETRAS3)
    NUMEROSRANDOM3 = random.sample(NUMEROS, CANTIDADNUMEROS3)
    SIMBOLOSRANDOM3 = random.sample(SIMBOLOS,CANTIDADSIMBOLOS3)

    # combinar letras, numeros y simbolos
    MEZCLA = LETRASRANDOM3 + NUMEROSRANDOM3 + SIMBOLOSRANDOM3
    # mezclar la cadena resultante de la suma de los 3 arreglos
    random.shuffle(MEZCLA)
    # unir los caracteres de los arreglos
    CONTRASENAGENERADA3 = "".join(MEZCLA)
    # imprimir la contraseña
    print("Su contraseña generada es:\n",CONTRASENAGENERADA3)
    print("Gracias por usar este programa")
else:
    print ("No existe esa opción")
