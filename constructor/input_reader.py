import re


def parse_vertex_and_square_ids(
    data: str, start_string: str = "Square ID", end_string: str = "# Edges",
) -> dict:
    """Return a dictionary of vertex ID & square ID pairs.

    This function will parse through the read-in input data between ''start_string'' and ''end_string''
    to return the filtered text in-between. 
    This text is then converted to a dictionary mapping vertex IDs to square IDs.

    :param data: read-in input file
    :type data: str
    :param start_string: starting string to search from, defaults to 'Square ID'
    :type start_string: str
    :param end_string: ending string to search until, defaults to '# Edges'
    :type end_string: str
    :return: a dictionary of vertex IDs & corresponding square IDs
    :rtype: dict
    """
    # split the data on the two strings
    list_of_ids = data.split(start_string)[-1].split(end_string)[0]
    # split the data on newline character
    list_of_ids = list_of_ids.split("\n")
    # remove empty strings that arose due to whitespace by using filter
    list_of_ids = list(filter(lambda x: x != "", list_of_ids))

    # create a dictionary of key-value pairs by splitting on the comma character
    ids_map = {}
    for i in list_of_ids:
        splitted_string = i.split(",")
        vertex_id = splitted_string[0]
        square_id = int(splitted_string[1])

        # create a mapping
        ids_map[vertex_id] = square_id

    return ids_map


def parse_edges_and_weights(
    data: str, start_string: str = "Distance", end_string: str = "# Source",
) -> list:
    """Return a list of edges with weights.
    
    This function will parse through the read-in input data between strings ''start_string'' and ''end_string''
    to return the filtered text in-between.
    This text is then converted to a list of sub-lists, where each sub-list is of the form:
    [from_vertex, to_vertex, weight].

    :param data: read-in input file
    :type data: str
    :param start_string: starting string to search from, defaults to 'Distance'
    :type start_string: str
    :param end_string: ending string to search until, defaults to '# Source'
    :type end_string: str
    :return: a list of lists of edges and weights
    :rtype: list
    """
    # split the data on the two strings
    list_of_edges = data.split(start_string)[-1].split(end_string)[0]
    # split the data on newline character
    list_of_edges = list_of_edges.split("\n")
    # remove empty strings that arose due to whitespace by using filter
    list_of_edges = list(filter(lambda x: x != "", list_of_edges))

    # create a list of lists of type [from, to, weight] by splitting on the comma character
    list_of_lists_edges = []
    for i in list_of_edges:
        splitted_string = i.split(",")
        # convert the splitted string elements to integer
        sublist_of_edges = [int(i) for i in splitted_string]
        # append the sublist to the major list
        list_of_lists_edges.append(sublist_of_edges)

    return list_of_lists_edges


def parse_src_and_dest(data: str) -> tuple:
    """Return source and destination vertices.
    
    This function will parse the read-in input data looking for vertex numbers after characters
    `S` for source and `D` for destination.
    The parsed vertex numbers are then converted to integers and returned.

    :param data: read-in input file
    :type data: str
    :return: source and destination vertices
    :rtype: tuple
    """
    # look for a sequence of digits the character S separated by newline
    regex_source = re.compile("S,([0-9]*)\n")
    # look for a sequence of digits after the character D separated by newline
    regex_dest = re.compile("D,([0-9]*)\n")

    # find the matches in data
    src = int(regex_source.findall(data)[0])
    dest = int(regex_dest.findall(data)[0])

    return src, dest


def compute_square_coordinates(height: int = 10, width: int = 10) -> list:
    """Compute coordinates of the bottom right corner for each square on the 10x10 grid.

    This function will store the coordinate information of the bottom right corner of each square for subsequent use.
    Indices in the resultant lists are equal to respective Square IDs.

    :param height: height of the grid, defaults to 10
    :type height: int
    :param width: width of the grid, defaults to 10
    :type width: int
    :return: list of approximate square coordinates
    :rtype: list
    """
    square_coordinates = []

    # initialize location of the top left corner of the grid (square 0)
    loc_x, loc_y = 0, 0

    # move down 10 times
    for i in range(height):
        loc_x = loc_x - height
        # move right 10 times
        for j in range(width):
            loc_y = loc_y + width
            square_coordinates.append((loc_x, loc_y))

    return square_coordinates
