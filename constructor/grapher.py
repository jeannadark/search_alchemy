from collections import defaultdict


class UGraph:
    """Constructs an undirected weighted graph."""

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src: int, dest: int, w: int) -> None:
        """Add weighted edges between source and destination vertices.
        
        :param src: source vertex
        :type src: int
        :param dest: destination vertex
        :type dest: int
        :param w: weight of the edge between src and dest
        :type w: int
        """
        w = w / 10  # divide by 10 to fix for grid size

        self.graph[src].append((dest, w))
        self.graph[dest].append((src, w))

    def get_weighted_neighbors(self, v_id: int) -> list:
        """Return the list of a vertex's neighbors & the respective edge weights.

        Each neighbor is a tuple of type (neighbor_id, weight).
        
        :param v_id: a given vertex id
        :type v_id: int
        :return: list of neighbors with weights
        :rtype: list
        """
        return self.graph[v_id]
