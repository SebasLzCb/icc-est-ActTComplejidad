# Benchmarking.py
"""
Clase responsable de medir el tiempo de ejecución de los algoritmos de ordenamiento.
Genera los datos que se utilizarán en la gráfica comparativa.
"""

import time
import random
from SortMethods import SortMethods

class Benchmarking:
    def __init__(self):
        # Instancia de la clase que contiene los algoritmos de ordenamiento
        self.sorter = SortMethods()

    def generar_datos(self, tamanos, repeticiones=1):
        """
        Genera los datos de rendimiento para cada algoritmo y tamaño de arreglo.
        Devuelve un diccionario con los tiempos de ejecución promedio.
        """
        resultados = {
            "Metodo Burbuja": [],
            "Metodo Burbuja Mejorado": [],
            "Metodo Insercion": [],
            "Metodo Seleccion": [],
            "Metodo Shell": []
        }

        for n in tamanos:
            # Arreglo base de números aleatorios entre 0 y 100000
            arreglo_base = [random.randint(0, 100000) for _ in range(n)]

            # Se mide el tiempo promedio para cada método usando una copia del arreglo base
            resultados["Metodo Burbuja"].append(self.tiempo_promedio(self.sorter.sort_burbuja, arreglo_base, repeticiones))
            resultados["Metodo Burbuja Mejorado"].append(self.tiempo_promedio(self.sorter.sort_burbuja_mejorado, arreglo_base, repeticiones))
            resultados["Metodo Insercion"].append(self.tiempo_promedio(self.sorter.sort_insercion, arreglo_base, repeticiones))
            resultados["Metodo Seleccion"].append(self.tiempo_promedio(self.sorter.sort_seleccion, arreglo_base, repeticiones))
            resultados["Metodo Shell"].append(self.tiempo_promedio(self.sorter.sort_shell, arreglo_base, repeticiones))

        return resultados

    def tiempo_promedio(self, metodo, arreglo, repeticiones):
        """
        Mide el tiempo de ejecución promedio de un método de ordenamiento.
        Recibe una función, el arreglo base y el número de repeticiones.
        """
        total = 0
        for _ in range(repeticiones):
            copia = arreglo[:]  # Copia para evitar ordenar un arreglo ya ordenado
            inicio = time.perf_counter()
            metodo(copia)
            fin = time.perf_counter()
            total += (fin - inicio)
        return total / repeticiones