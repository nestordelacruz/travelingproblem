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


generated_graph = graph(10)
print(generated_graph)

def nearest_neighboor(graph):
    # Iniciamos en cualquier nodo, en este caso supongamos el primero del grafo generado
    startingPoint = 0

    # Recorrido encontrado (considerando que el punto de partida es el inicial)
    path = [startingPoint]

    counter = 1
    # Crear una lista de nodos que pueden ser visitados
    nodes = list(range(len(graph[0])))
    # Variable de costo que se actualiza con cada iteracion para determinar el costo total de la ruta encontrada
    totalCost = 0
    while(counter < len(graph[0])):
        # Excluir todos los nodos visitados y el nodo raiz
        nodes = [x for x in nodes if x != startingPoint]

        # Agarrar el valor maximo como el minimo de forma inicial
        min = max(graph[startingPoint])

        # Identificar las posibles ciudades por traversar considerando que ya visitamos ciertas ciudades, que no debe
        # de visitarse a si mismo y que se quiere visitar al nodo con menor costo
        for index, possible_city in enumerate(graph[startingPoint]):
            # Si la ciudad no ha sido recorrida entonces es candidato
            if index in nodes:
                # Si el costo encontrado es menor guardar el indice para descartar la busqueda de dicho nodo para traversos futuros
                if possible_city <= min:
                    min = possible_city
                    indexPosition = index

        # Actualizar punto de partida a que ahora sea con el indice correspondiente al del valor minimo (como si fuera un recorrido)
        startingPoint = indexPosition
        # Agregar el costo de la ruta encontrada
        totalCost += min

        # Agregar la ruta de partida encontrada
        path.append(startingPoint)
        counter += 1

    print("------ NEAREST NEIGHBOOR HEURISTIC ------")
    print("CAMINO ENCONTRADO: ", path)
    print("COSTO TOTAL DE LA RUTA: ", totalCost)

nearest_neighboor(generated_graph)