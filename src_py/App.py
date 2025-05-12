"""
Archivo principal que conecta todos los componentes del proyecto.
Ejecuta las pruebas de rendimiento y muestra la gráfica resultante.
"""

from Benchmarking import Benchmarking
from Grafica import Grafica

def main():
    print("---------- Programa funcionando ----------\n")
    
    tamanos = [10000, 30000, 50000, 100000]  # Tamaños de arreglo a probar
    benchmarking = Benchmarking()             # Instancia para pruebas de rendimiento

    print("----- Benchmarking iniciado -----\n")
    resultados = benchmarking.generar_datos(tamanos, repeticiones=1)  # Ejecuta los algoritmos y guarda resultados

    grafica = Grafica()                       # Instancia para graficar resultados
    grafica.mostrar(resultados, tamanos)

    print("\nResultados de tiempo de ejecución (en segundos):")
    for metodo, tiempos in resultados.items():
        print(f"{metodo}: {tiempos}")

if __name__ == "__main__":
    main()