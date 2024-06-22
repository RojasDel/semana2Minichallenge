import random
import string

def generar_contraseña(longitud):
    if longitud < 8 or longitud > 16:
        raise ValueError("La longitud debe estar entre 8 y 16 caracteres.")

    # Definir los posibles caracteres que pueden estar en la contraseña
    letras_mayusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation

    # Combinar todos los caracteres posibles
    todos_caracteres = letras_mayusculas + letras_minusculas + numeros + simbolos

    # Generar una contraseña que cumpla con los requisitos
    contraseña = [
        random.choice(letras_mayusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]

    # Completar la contraseña con caracteres aleatorios hasta alcanzar la longitud deseada
    contraseña += random.choices(todos_caracteres, k=longitud-4)

    # Mezclar los caracteres para que no sigan un patrón predecible
    random.shuffle(contraseña)

    # Convertir la lista de caracteres en una cadena
    return ''.join(contraseña)

# Solicitar al usuario que ingrese la longitud deseada para la contraseña
longitud_deseada = int(input("Introduce la longitud deseada para la contraseña (entre 8 y 16): "))

# Generar y mostrar la contraseña segura
try:
    contraseña_segura = generar_contraseña(longitud_deseada)
    print("Contraseña segura generada:", contraseña_segura)
except ValueError as e:
    print(e)
