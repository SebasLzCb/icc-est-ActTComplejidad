# Teoría de la Complejidad

## 📌 Información General

**Título:** Análisis de la Teoría de la Complejidad  
**Asignatura:** Estructura de Datos  
**Carrera:** Computación  
**Estudiantes:** Sebastian Loza 
**Fecha:** Cuenca, 11 de mayo de 2025  
**Profesor:** Ing. Pablo Torres

---

## 🛠️ Descripción

Este proyecto tiene como objetivo introducir los fundamentos de la teoría de la complejidad, centrándose en el análisis del rendimiento de los algoritmos. Se abordan los conceptos fundamentales para evaluar la eficiencia algorítmica desde el punto de vista teórico y práctico. Entre los temas principales se incluyen:

- **Coste temporal:** mide el tiempo que tarda un algoritmo en ejecutarse.
- **Coste espacial:** determina la cantidad de memoria utilizada.
- **Factores que influyen en el tiempo de ejecución:** tanto propios del algoritmo como del entorno donde se ejecuta.
- **Análisis teórico y análisis experimental del rendimiento.**
- **Notaciones asintóticas:** Big O (O), Omega (Ω) y Theta (Θ), aplicadas a los casos mejor, peor y promedio.

---

## Ejecución del Proyecto

Para compilar y ejecutar el proyecto desde consola:

```bash
# Compilación del código Java
javac App.java

# Ejecución del programa
java App
```

🧑‍💻 Ejemplo de Salida del Programa
```bash
----------Programa Funciona----------

-----Benchmarking funcionando-----
```
##  Captura de Pantalla
(Inserta aquí una imagen del gráfico o salida del benchmarking si tienes)

📁 Estructura del Proyecto
plaintext
Copiar
Editar
icc-est-u1-teoriaDeComplejidad
├── README.md
├── .vsCode/
├── bin/
│   └── App.class
├── src/
├── src_py/
│   ├── App.py
│   ├── Benchmarking.java
│   ├── Grafica.py
│   └── SortMethods.java
📘 Contenido del Código Java Principal
App.java

java
Copiar
Editar
public class App {
    public static void main(String[] args) {
        System.out.println("----------Programa Funciona----------");
        Benchmarking.main(args);  // Ejecuta el benchmarking
    }
}
Benchmarking.java

java
Copiar
Editar
public class Benchmarking {
    public static void main(String[] args) {
        System.out.println("-----Benchmarking funcionando-----");
        // Aquí iría la lógica de benchmarking de algoritmos de ordenamiento
    }
}
🧠 Conclusión
La práctica sobre la teoría de la complejidad permitió comprender cómo se mide la eficiencia de los algoritmos a través de funciones de crecimiento y notaciones asintóticas como Big O, Ω (Omega) y Θ (Theta). Estas herramientas son esenciales para predecir el comportamiento de un algoritmo frente a entradas de distintos tamaños y en diferentes escenarios: mejor, peor y promedio caso.

Además, se analizó el impacto que tienen tanto el coste temporal como el espacial, reconociendo que la elección de un algoritmo debe considerar no solo la teoría, sino también el contexto práctico de ejecución.