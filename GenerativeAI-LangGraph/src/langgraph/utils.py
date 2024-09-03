def print_graph_info(graph):
    """
    Prints basic information about a graph.
    """
    print(f"Number of nodes: {len(graph.nodes)}")
    print(f"Number of edges: {len(graph.edges)}")

def save_graph_to_file(graph, filename):
    """
    Saves a graph to a file.
    """
    with open(filename, 'w') as f:
        f.write(graph.to_json())