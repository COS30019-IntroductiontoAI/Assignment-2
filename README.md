<<<<<<< Updated upstream
# Assignment 2A – Greedy Best First Search

## Overview
This project implements the **Greedy Best-First Search (GBFS)** algorithm for path finding in a weighted graph.
The program reads a graph from a text file, applies GBFS using a selected heuristic function, and outputs a path from the origin node to one or more destination nodes.

The implementation supports multiple heuristics (CUS1), including **Euclidean** and **Manhattan** distance, which can be selected at runtime.

---

## How to run
```bash
python search.py PathFinder-test.txt GBFS
python search.py PathFinder-test.txt GBFS euclidean
python search.py PathFinder-test.txt GBFS manhattan
```

## Examples
Example command:
```bash
python search.py PathFinder-test.txt GBFS euclidean
```
Example output:

```
5 3
2 -> 3 -> 5
4 3
2 -> 1 -> 4
```
Each result shows:

- The destination node ID
- The number of nodes in the path
- The path from the origin to the destination
=======
# A\* Search - Instructions

This project implements a tree-based A\* search for a route-finding assignment.

## Requirements

- Python 3.x

## Run

```bash
python search.py <filename> AS
```

Example:

```bash
python search.py PathFinder-test.txt AS
```

## Input File Format

The input file is plain text with these sections:

- `Nodes:`
  - Each line: `id: (x,y)`
- `Edges:`
  - Each line: `(from,to): cost`
- `Origin:`
  - One line with the origin node id
- `Destinations:`
  - One line with destination ids separated by `;`

Example:

```
Nodes:
1: (4,1)
2: (2,2)
Edges:
(1,2): 5
Origin:
1
Destinations:
2; 3
```

## Notes (Assignment Behavior)

- Tree-based A\* (no closed list, no cost updates)
- Stops when any destination is reached
- Edge costs must be non-negative
- Node ids in `Origin`, `Destinations`, and `Edges` must exist in `Nodes`

## Output Format

For valid input and `AS` method, output is:

```
<filename> A*
<goal> <generated_node_count> (number of nodes)
<space-separated path> (path)
```
>>>>>>> Stashed changes
