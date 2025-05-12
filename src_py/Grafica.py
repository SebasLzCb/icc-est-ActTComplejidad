# Grafica.py
"""
Clase encargada de graficar los resultados de tiempo de ejecución de los algoritmos.
Utiliza matplotlib para generar y mostrar la gráfica.
"""

import matplotlib.pyplot as plt
from datetime import datetime

class Grafica:
    def mostrar(self, resultados, tamanos):
        """
        Muestra una gráfica de líneas con los resultados de todos los métodos
        comparando el tiempo de ejecución frente al tamaño del arreglo.
        """
        fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        plt.figure(figsize=(12, 6))

        # Agrega una línea por cada algoritmo
        for metodo, tiempos in resultados.items():
            plt.plot(tamanos, tiempos, marker='o', label=metodo)

        plt.title(f"Sebastian Loza - {fecha_actual}", fontsize=14, fontweight='bold')
        plt.xlabel("Tamaño del arreglo")
        plt.ylabel("Tiempo de ejecución (s)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("grafica_comparativa.png")
        plt.show()