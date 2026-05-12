import time

def busqueda_secuencial(lista, objetivo):
    """
    Realiza una búsqueda secuencial en la lista.
    Retorna la posición si se encuentra, de lo contrario -1.
    """
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def cargar_datos(nombre_archivo):
    """Lee los números del archivo y los retorna como una lista de enteros."""
    numeros = []
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                # Se limpia la línea y se convierte a entero
                valor = linea.strip()
                if valor:
                    numeros.append(int(valor))
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no fue encontrado.")
    except ValueError:
        print("Error: El archivo contiene datos que no son números válidos.")
    return numeros

def main():
    nombre_archivo = "datos.txt"
    
    print("Cargando datos...")
    lista_numeros = cargar_datos(nombre_archivo)
    
    if not lista_numeros:
        return

    print(f"Se cargaron {len(lista_numeros)} números.")
    
    # Ordenar los números
    print("Ordenando números...")
    lista_numeros.sort()
    print("Lista ordenada con éxito.")

    while True:
        try:
            entrada = input("\n¿Qué número desea buscar? (o escribe 'salir' para terminar): ")
            if entrada.lower() == 'salir':
                break
            
            objetivo = int(entrada)
            
            # Medir el tiempo de búsqueda
            inicio_tiempo = time.perf_counter()
            posicion = busqueda_secuencial(lista_numeros, objetivo)
            fin_tiempo = time.perf_counter()
            
            # Calcular tiempo en milisegundos
            tiempo_ms = (fin_tiempo - inicio_tiempo) * 1000
            
            if posicion != -1:
                print(f"Número {objetivo} encontrado en la posición {posicion}.")
            else:
                print(f"El número {objetivo} no se encuentra en la lista.")
            
            print(f"Tiempo de búsqueda: {tiempo_ms:.4f} ms")
            
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()