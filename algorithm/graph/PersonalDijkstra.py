import queue


def dijkstra(graph, start_node):
    distance_list = list()
    distance_list[start_node] = 0
    adjacent_queue = queue.PriorityQueue()
    adjacent_queue.put(start_node)

    while adjacent_queue:
        target_node = adjacent_queue.get()
        adjacent_nodes = graph[target_node]

        for adjacent_node in adjacent_nodes:
            if graph[target_node][adjacent_node] != -1:
                if distance_list[adjacent_node] > distance_list[target_node] + graph[target_node][adjacent_node]:
                    distance_list[adjacent_node] = distance_list[target_node] + graph[target_node][adjacent_node]
                    adjacent_queue.put(adjacent_node)

    return distance_list

