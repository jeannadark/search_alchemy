# Uninformed and Informed Search

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites-and-installation">Prerequisites and Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#how-it-works">How It Works</a></li>
      <ul>
    <li><a href="#performance-comparison">Performance Comparison</a></li>
      </ul>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

The goal of this project is to enable uninformed and informed graph search on a 10x10 square grid.

Specifically, a program should be implemented that
- reads the graph data, consisting of square and vertex IDs, edges and their weights, and
- calculates the shortest path from start vertex to goal vertex.

The graph nodes are located on a 10x10 square grid, where each square is of size 10x10.

Two search strategies are implemented and compared:
- uninformed (UCS - Uniform Cost Search),
- informed (A-star).

### Built With

The following main external libraries were used to build this project:
- <a href="https://docs.python.org/3/library/queue.html">queue</a>

<!-- GETTING STARTED -->
## Getting Started

This is a list of instructions on how anyone can get started with this code.

### Prerequisites & Installation

1. Clone the repo
```sh
    git clone https://github.com/njamalova/search_alchemy.git
```
2. Install packages, if not installed
```sh
    pip install queue
```

<!-- USAGE EXAMPLES -->
## Usage

To run this code, one argument is taken from the command line: file name.

Example of how to run the program:
``` sh
    find_shortest_path.py somefile.txt
```
If the file is not found, the default `p1_graph.txt` in this directory is used instead.

Any inputted file should follow the same format as the default to enable accurate parsing of graph data.

## How It Works

1. module ``find_shortest_path.py`` contains the function ``runner()`` that parses the data, constructs the graph and computes the shortest path using two search strategies. Shortest path information is then printed to the console, i.e. cost of the path, path itself and run-time of each implemented strategy.
2. module ``input_reader.py`` contains such functions as ``parse_vertex_and_square_ids()``, ``parse_edges_and_weights()`` and ``parse_src_and_dest()`` that read the input file in the appropriate format.
3. module ``grapher.py``contains the undirected graph class ``UGraph`` that constructs the graph by using the parsed graph edge data.
4. module ``searcher.py`` contains the ``AlgoSearcher`` class that implements informed and uninformed searches on the undirected graph.

The heuristic function that was implemented within the ``AlgoSearcher`` class works as follows:

It computes the square root of the Euclidian distance between the current vertex and the goal vertex by using the coordinates of the bottom right corners of the squares to which vertices belong. This helps provide a sense of direction to the informed graph search, whereby movement in any direction is allowable.

### Performance Comparison

For the default-given start and goal vertices (0 and 99), the performance of A* vs UCS is as follows:

|  Metric  |      A*       |   UCS    |
|----------|:-------------:|---------:|
| visited  |  34 nodes     | 73 nodes |
| run-time |  ~0.003 sec   | ~0.003 sec|

Not a lot of benefit gained in terms of performance for A* (perhaps because it’s relatively a small graph), but it does expand fewer nodes and is as optimal as UCS in finding the shortest path.
