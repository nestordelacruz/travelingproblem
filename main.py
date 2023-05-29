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

def nearest_neighbor(graph):
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
    return path
    
def optimize_path(graph, path):
    best_path = path  # Almacenamos el mejor camino encontrado hasta el momento
    best_cost = calculate_path_cost(graph, best_path)  # Calculamos el costo del mejor camino
    improved = True  # Bandera para indicar si se ha realizado una mejora

    while improved:  # Repetimos hasta que no se pueda realizar más mejoras
        improved = False  # Inicialmente no se ha realizado ninguna mejora

        # Iteramos sobre todos los pares de nodos i y j en el camino
        for i in range(1, len(path) - 2):
            for j in range(i + 1, len(path)):
                if j - i == 1:
                    continue  # No se realiza la mejora si los nodos son adyacentes

                new_path = path[:]  # Creamos una copia del camino actual
                new_path[i:j] = path[j - 1:i - 1:-1]  # Invertimos el subsegmento entre i y j

                new_cost = calculate_path_cost(graph, new_path)  # Calcular el costo del nuevo camino

                if new_cost < best_cost:  # Si el costo es menor que el mejor costo actual
                    best_path = new_path  # Actualizamos el mejor camino
                    best_cost = new_cost  # Actualizamos el mejor costo
                    improved = True  # Indicamos que se ha realizado una mejora

        path = best_path  # Actualizamos el camino actual con el mejor camino encontrado en esta iteración
    print("------ 2-OPT OPTIMIZATION ------")
    print("CAMINO OPTIMIZADO: ", best_path)
    print("COSTO OPTIMIZADO: ", calculate_path_cost(graph, best_path))
    return best_path  # Devolvemos el mejor camino encontrado

def calculate_path_cost(graph, path):
    total_cost = 0
    for i in range(len(path) - 1):
        start = path[i]
        end = path[i + 1]
        total_cost += graph[start, end]

    return total_cost

def main():
    num_of_cities = 30
    generated_graph = graph(num_of_cities)
    print(generated_graph)
    initial_path = nearest_neighbor(generated_graph)
    optimized_path = optimize_path(generated_graph, initial_path)


main()