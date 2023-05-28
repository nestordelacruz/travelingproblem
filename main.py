import random
import numpy as np

# Generacion de un grafo simetrico y que sigue Triangle Inequality
def graph(vertices):
    # Crear matriz que identifica la conexion entre los nodos del grafo
    graph = np.zeros((vertices, vertices))

    # Generacion de un valor aleatorio entre dos nodos (para una arista)
    for i in range(vertices):
        for j in range(i + 1, vertices):
            cost = random.randint(1, 50)
            graph[i, j] = cost
            graph[j, i] = cost

    # Asegurar la propiedad de Triangle Inequality sobre el grafo
    # De un vertice
    for start in range(vertices):
        # Para las posibles rutas, donde j sirve como intermediario
        for interm in range(vertices):
            # Para las posibles rutas, donde k plantea el fin de la ruta
            for end in range(vertices):
                if start != interm and interm != end and start != end:
                    # Si el valor de la suma entre un nodo + intermediario + end es menor a solamente pasarl de start a end entonces
                    # el valor debe ser modificado ya que no cumple con la propiedad de Triangle Inequality
                    if graph[start, interm] + graph[interm, end] < graph[start, end]:
                        # Se actualiza el valor entre start y end con la suma que ocasionaba dicha inecualidad
                        graph[start, end] = graph[start, interm] + graph[interm, end] 

    return graph


# Ejemplo de generacion de un grafo simetrico y que sigue la propiedad de Triangle Inequality
generated_graph = graph(5)
print(generated_graph)