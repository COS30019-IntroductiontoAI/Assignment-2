# COS30019 – Assignment 2A  
## Tree-Based Search – Route Finding Problem

---

## Team Members

| Name | Student ID |
|------|------------|
| Do Gia Huy (leader) | 104988294 |
| Le Thanh Nam | 104999380 |
| Huynh Doan Hoang Minh | 104777308 |
| Bui Quang Doan | 104993227 |

---

# 1. Project Overview

This project implements **tree-based search algorithms** to solve the Route Finding Problem on a 2D graph.

The objective is to find a path from an **Origin node** to one of the **Destination nodes** using the required search strategy.

Each problem file contains:

- A set of nodes with 2D coordinates  
- A set of directed edges with associated costs  
- One origin node  
- One or multiple destination nodes  

The search terminates when **any one** of the destination nodes is reached.

---

# 2. Implemented Search Algorithms


## Uninformed Methods

### 1. DFS – Depth First Search
- Expands the deepest node first  
- Uses a stack (LIFO)  
- Does not guarantee optimal solution  

### 2. BFS – Breadth First Search
- Expands nodes level by level  
- Uses a queue (FIFO)  
- Finds shortest path in terms of number of edges when costs are uniform  

### 3. CUS1 – Iterative Deepening Search (IDS)
- Repeatedly performs depth-limited DFS  
- Gradually increases depth limit  
- Combines memory efficiency of DFS with completeness of BFS  
- Guarantees optimal solution in terms of depth  

--

## Informed Methods

### 4. GBFS – Greedy Best First Search
- Uses heuristic function h(n)  
- Expands node that appears closest to goal  
- Does not consider path cost g(n)  
- Not guaranteed optimal  

### 5. AS – A* Search
- Uses evaluation function:

  f(n) = g(n) + h(n)

  where:  
  - g(n) = cost from start to current node  
  - h(n) = heuristic estimate to nearest goal  

- Guarantees optimal solution if heuristic is admissible  

### 6. CUS2 – Iterative Deepening A* (IDA*)
- Combines A* evaluation with iterative deepening  
- Uses f-cost threshold  
- Memory efficient compared to A*  
- Guaranteed optimal if heuristic is admissible  

---

# 3. Heuristic Function

For informed searches (GBFS, AS, CUS2), we use:

**Euclidean Distance**

h(n) = distance from node n to the closest destination

This ensures:

- Admissibility in geometric test cases  
- Consistency in realistic map scenarios  

Some trap tests intentionally violate geometric proportionality to evaluate algorithm robustness.

---

# 4. Program Execution

The program runs from the command line:

```bash
python search.py <filename> <method>
```

Example:

```bash
python search.py test1_simple_cycle.txt bfs
```

Where:

- `<filename>` is the problem file  
- `<method>` is one of:

```bash
DFS
BFS
GBFS
AS
CUS1
CUS2
```


---

# 5. Output Format

When a goal is reached, the program outputs:

```bash
filename method
goal number_of_nodes
path
```

Where:

- `goal` = destination reached  
- `number_of_nodes` = total nodes generated during search  
- `path` = sequence from origin to goal  

If no solution exists, the program reports failure.

---

# 6. Core Design Concepts

## Tree-Based Search

- Each search builds a search tree from scratch  
- No global graph-level pruning beyond algorithm rules  
- Node expansion strictly follows assignment ordering requirements  

## Expansion Order Rule

When all else is equal:

1. Expand smaller node number first  
2. If still equal, expand in chronological order (earlier generated first)  

This ensures deterministic behavior.

## Multi-Destination Handling

- The search stops when the first goal is reached  
- For heuristic methods, the nearest goal is used in h(n)

---

# 7. Test Cases

We created **10 test cases** covering different scenarios.

| Test File | Purpose |
|------------|----------|
| test1_simple_cycle | Cycle handling |
| test2_priority_trap_cycle | Deep misleading branch |
| test3_undirected_cycle | Realistic weighted graph |
| test4_local_maximum_minimum_trap | Greedy trap scenario |
| test5_cost_trap | Cost deception scenario |
| test6_complex_multiplegoal_trap | Multiple goals + trap |
| test7_disconnected_graph | No path available |
| test8_start_is_goal | Origin equals destination |
| test9_all_else_is_equal | Tie-breaking behavior |
| test10_complex_map | Large realistic map |

## Test Design Coverage

The test suite includes:

- Cycles  
- Directed and undirected edges  
- Weighted graphs  
- Uniform-cost graphs  
- Multiple destinations  
- Disconnected graphs  
- Heuristic traps  
- Tie-breaking cases  
- Edge cases (start equals goal)  

This ensures broad evaluation of algorithm behavior.

---

# 8. Features Implemented

- All 6 required search methods  
- Support for multiple destinations  
- Deterministic expansion ordering  
- CLI-based execution  
- 10 structured test cases  
- Heuristic-based informed search  
- Tree-based node generation counting  

---

# 9. Known Limitations

- CLI version only (no GUI)  
- IDS and IDA* may take longer on large graphs  
- No advanced optimizations beyond standard algorithm definitions  

---

# 10. Report (Separate Document)

The report includes:

- Explanation of the Route Finding Problem  
- Description of implemented algorithms  
- Testing results  
- Performance comparison  
- Insights obtained from experimentation  
- Discussion on optimal strategy choice  
- Possible improvements  

---