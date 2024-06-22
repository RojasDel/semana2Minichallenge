colores = input('Escribe las claves separadas por comas y luego enter: ').split(',')
colores_asociados_a = input('Escribe los valores separados por comas y luego enter: ').split(',')

lista_completa = {}

if len(colores) != len(colores_asociados_a):
    print('Ambas listas deben tener la misma longitud!')

else:
    for i in range(len(colores)):
     lista_completa[colores[i].strip()]= colores_asociados_a[i].strip()

print('Diccionario creado ', lista_completa)
