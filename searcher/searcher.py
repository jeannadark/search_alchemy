from queue import PriorityQueue
import numpy as np


class AlgoSearcher:
    """Implements uninformed and informed graph search strategies on a given graph."""

    def __init__(self, graph: dict, coordinates: list, ids: dict):
        """Perform initialization.

		:param graph: the provided graph on which search is performed
		:type graph: dict
		:param coordinates: coordinates of each square's top right corner on a 10x10 grid
		:type coordinates: list
		:param ids: mapping of vertex ids to square ids
		:type ids: dict
		"""
        self.graph = graph
        self.coordinates = coordinates
        self.ids = ids

    def get_coordinates(self, v_id: int) -> tuple:
        """Return coordinates of the bottom right corner of the square to which the vertex belongs.

		This function will help to compute heuristic cost by using approximate square coordinate information.

		:param v_id: a given vertex id
		:type v_id: int
		:return: (x, y) coordinates of the square id corresponding to vertex id
		:rtype: tuple
		"""
        square_id = self.ids[str(v_id)]
        x, y = self.coordinates[square_id]

        return x, y

    def compute_euclidian_distance(self, current_v: int, goal_v: int) -> float:
        """Return heuristic cost for A-star informed search.
		
		This function will compute the square root of Euclidian distance between the current vertex and the goal vertex
		by using the coordinates of the bottom right corners of the squares on which the vertices stand.
		This will help provide a sense of direction to the informed graph search,
		whereby movement in any direction is allowable.

		:param current_v: the current vertex
		:type current_v: int
		:param goal_v: the destination vertex for the search
		:type goal_v: int
		:return: square root of euclidian distance between the top right corners of squares to which vertices belong
		:rtype: float
		"""
        (x1, y1) = self.get_coordinates(current_v)
        (x2, y2) = self.get_coordinates(goal_v)

        euclidian_distance = np.sqrt(np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))

        return euclidian_distance

    def compute_shortest_path(self, src: int, dest: int, strategy: str) -> float:
        """Perform uniform cost search or A-star search on a given graph.
		
		This function will find the cost of the shortest path according to the chosen strategy.
		If the chosen strategy is UCS, then nodes are expanded according to the least path cost from the source.
		If the chosen strategy is A-star, the nodes are expanded according to the lowest total cost f(n),
		which is the sum of cost so far to reach that node (g(n)) and heuristic cost (h(n)).
		Priority queue is used to sort by lowest cumulative cost. Neighbor nodes are expanded if they are not visited yet, 
		or if the new path cost to the neighbor node is lower than the one computed previously.

		:param src: source vertex
		:type src: int
		:param dest: destination vertex
		:type dest: int
		:param strategy: either "ucs" or "a-star"
		:type strategy: str
		:return: shortest path cost between src and dest
		:rtype: float
		"""
        queue = PriorityQueue()
        queue.put((0, src))

        # stores shortest cost to each vertex
        shortest_cost = {}
        shortest_cost[src] = 0

        # stores the parent of each vertex
        self.parents = {}

        # counter
        cnt = 0

        while not queue.empty():
            total_cost, present_node = queue.get()

            # increment counter
            cnt += 1

            if present_node == dest:
                print("\nExpanded {} nodes.\n".format(cnt))
                return shortest_cost[dest]

            for next_node in self.graph.get_weighted_neighbors(present_node):
                neighbor, weight = next_node
                # update total cumulative cost to the neighbor node
                updated_shortest_cost = shortest_cost[present_node] + weight

                # go to the neighbor node only if it's not visited yet or if the updated cost is lower than previously computed
                if (
                    neighbor not in shortest_cost.keys()
                    or updated_shortest_cost < shortest_cost[neighbor]
                ):
                    shortest_cost[neighbor] = updated_shortest_cost

                    # add heuristic cost depending on chosen search strategy
                    if strategy.lower() == "a-star":
                        heuristic_cost = self.compute_euclidian_distance(neighbor, dest)
                    else:
                        heuristic_cost = 0

                    total_cost = shortest_cost[neighbor] + heuristic_cost

                    queue.put((total_cost, neighbor))

                    # update the parent vertex for the neighbor node
                    self.parents[neighbor] = present_node

        return shortest_cost[dest]

    def print_shortest_path(self, src: int, dest: int) -> None:
        """Print the shortest path between source and destination vertices.
		
		This function will keep appending the parent of each node until it finds the node whose parent is the source.
		It will then print the resultant reversed path.

		:param src: source vertex
		:type src: int
		:param dest: destination vertex
		:type dest: int
		"""
        shortest_path = [dest]
        while shortest_path[-1] != src:
            shortest_path.append(self.parents[shortest_path[-1]])
        shortest_path.reverse()
        print(shortest_path)
