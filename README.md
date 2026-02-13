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
