from functools import reduce


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = new_paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
        for new_path in new_paths:
            paths.append(new_path)
    return paths


def calculate_loss(num_nodes, g, loss, circuit):
    from_, to_, cost = circuit
    path = find_all_paths(g, from_, to_)
    idx = {i: j for i, j in zip(range(num_nodes), loss)}
    sum_ = reduce(lambda x, y: x + y, [idx[i] for i in path[0]])
    if sum_ == cost:
        return "APPROVED"
    else:
        return "REJECTED"
