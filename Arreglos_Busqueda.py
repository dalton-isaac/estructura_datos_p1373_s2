import time

# 1. Crear arreglo del 1 al 1,000,000 y pedir el dato
arreglo = list(range(1, 1000001))
objetivo = int(input("Ingresa el número a buscar: "))

print("\nResultados:")

#BÚSQUEDA SECUENCIAL
inicio = time.time()
pos_sec = -1  # Empezamos asumiendo que no lo encontramos (-1)

for i in range(len(arreglo)):
    if arreglo[i] == objetivo: 
        pos_sec = i  # Guardamos la posición
        break        # Detenemos el ciclo porque ya lo encontramos

fin = time.time()
print(f"Secuencial -> Posición: {pos_sec} | Tiempo: {fin - inicio:.6f} segundos")


#BÚSQUEDA BINARIA
inicio = time.time()
pos_bin = -1  # Empezamos asumiendo que no lo encontramos (-1)
izq = 0
der = len(arreglo) - 1

while izq <= der:
    medio = (izq + der) // 2
    
    if arreglo[medio] == objetivo: 
        pos_bin = medio  # Guardamos la posición
        break            # Detenemos el ciclo porque ya lo encontramos
    elif arreglo[medio] < objetivo: 
        izq = medio + 1
    else: 
        der = medio - 1

fin = time.time()
print(f"Binaria    -> Posición: {pos_bin} | Tiempo: {fin - inicio:.6f} segundos")