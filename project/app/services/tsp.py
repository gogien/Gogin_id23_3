from app.schemas.graph import Graph, PathResult
import networkx as nx


def solve_tsp(graph: Graph) -> PathResult:
    # Create a NetworkX graph
    G = nx.Graph()
    
    # Add nodes
    G.add_nodes_from(graph.nodes)
    
    # Add edges
    for edge in graph.edges:
        G.add_edge(edge[0], edge[1], weight=1)
    
    # Find a simple path visiting all nodes (this is a naive implementation)
    try:
        path = list(nx.dfs_preorder_nodes(G, source=graph.nodes[0]))
        # Add the first node at the end to complete the cycle
        path.append(path[0])
        return PathResult(path=path, total_distance=float(len(path) - 1))
    except nx.NetworkXError:
        return PathResult(path=[], total_distance=0.0) 