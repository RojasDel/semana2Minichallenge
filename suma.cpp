#include <iostream>  // Incluye la biblioteca de entrada y salida

int main() {
    // Declaraci�n de variables
    int num1, num2, suma;

    // Pedir al usuario el primer n�mero
    std::cout << "Por favor, introduce el primer numero: ";
    std::cin >> num1;  // Lee el primer n�mero y lo almacena en num1

    // Pedir al usuario el segundo n�mero
    std::cout << "Por favor, introduce el segundo numero: ";
    std::cin >> num2;  // Lee el segundo n�mero y lo almacena en num2

    // Sumar los dos n�meros
    suma = num1 + num2;

    // Mostrar el resultado de la suma
    std::cout << "La suma de " << num1 << " y " << num2 << " es " << suma << std::endl;

    return 0;  // Termina el programa
}

