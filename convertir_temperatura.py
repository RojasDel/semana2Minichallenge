def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Solicitar al usuario que elija el tipo de conversión
opcion = input("Elige el tipo de conversión (1: Celsius a Fahrenheit, 2: Fahrenheit a Celsius): ")

# Realizar la conversión según la opción elegida
if opcion == '1':
    celsius = float(input("Introduce la temperatura en Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
elif opcion == '2':
    fahrenheit = float(input("Introduce la temperatura en Fahrenheit: "))
    celsius = fahrenheit_a_celsius(fahrenheit)
    print(f"{fahrenheit} grados Fahrenheit son {celsius} grados Celsius.")
else:
    print("Opción no válida. Por favor inicia nuevamente el programa, elige 1 o 2.")
