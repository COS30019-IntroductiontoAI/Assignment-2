# Assignment 2A – Greedy Best First Search

## Overview
This project implements the **Greedy Best-First Search (GBFS)** algorithm for path finding in a weighted graph.
The program reads a graph from a text file, applies GBFS using a selected heuristic function, and outputs a path from the origin node to one or more destination nodes.

The implementation supports multiple heuristics (CUS1), including **Euclidean** and **Manhattan** distance, which can be selected at runtime.

---

## How to run

python search.py PathFinder-test.txt GBFS
python search.py PathFinder-test.txt GBFS euclidean
python search.py PathFinder-test.txt GBFS manhattan

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
