from constructor import input_reader, grapher
from searcher import searcher
import time


def runner(filename: str) -> None:
    """Parses provided input data, constructs a graph and finds the shortest path between source and goal vertices.
    
    :param filename: the name of the input file to parse
    :type filename: str
    """
    f = open(filename, "r")
    text = f.read()

    ## -- parsing -- ##

    # parse edge data
    edges = input_reader.parse_edges_and_weights(data=text)
    # parse vertex and square ids
    ids_map = input_reader.parse_vertex_and_square_ids(data=text)
    # parse start and goal vertices
    start, goal = input_reader.parse_src_and_dest(data=text)

    ## -- compute approximate coordinates on a height x width grid -- ##

    coordinates = input_reader.compute_square_coordinates(height=10, width=10)

    ## -- construct a graph -- ##

    graph = grapher.UGraph()
    for edge_info in edges:
        vertex_from = edge_info[0]
        vertex_to = edge_info[1]
        weight = edge_info[2]
        graph.add_edge(vertex_from, vertex_to, weight)

    ## -- start searching for shortest path -- ##

    search = searcher.AlgoSearcher(graph=graph, coordinates=coordinates, ids=ids_map)

    # perform uninformed uniform cost search
    print("\nPerforming UCS ...")

    start_time = time.time()
    shortest_cost = search.compute_shortest_path(src=start, dest=goal, strategy="ucs")
    end_time = time.time()

    print("UCS found this as the shortest path cost: {}\n".format(shortest_cost))
    print("UCS found this shortest path, in order:\n")
    search.print_shortest_path(src=start, dest=goal)
    print("\nUCS elapsed time: {}\n".format(end_time - start_time))

    # perform informed A-star search
    print("\nPerforming A* ...")

    start_time = time.time()
    shortest_cost = search.compute_shortest_path(
        src=start, dest=goal, strategy="a-star"
    )
    end_time = time.time()

    print("A* found this as the shortest path cost: {}\n".format(shortest_cost))
    print("A* found this shortest path, in order:\n")
    search.print_shortest_path(src=start, dest=goal)
    print("\nA* elapsed time: {}\n".format(end_time - start_time))


if __name__ == "__main__":

    try:
        input_file = str(input("Please enter the full filename: \n"))
        runner(filename=input_file)

    except FileNotFoundError:
        print("Invalid filename. Using default filename in this directory instead.")
        input_file = "p1_graph.txt"
        runner(filename=input_file)
