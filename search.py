import sys
from parser import parse_problem_file
from algorithms.cus2 import IDA_Star
from algorithms.gbfs import gbfs
from algorithms.cus1 import cus1
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.astar import astar_search

def main():
  # Check whether the command line argument is acceptable or not
  if len(sys.argv) != 3:
    print("The correct format is 'python search.py <file_name> <method>'!")
    return

  # Read the argument from the command line
  filename = sys.argv[1]
  method = sys.argv[2].lower()

  # Parse the problem first
  graph, start_id, goal_ids = parse_problem_file(filename)

  path = []
  node_count = 0
  total_cost = 0

  # Solve and return the result
  if method == "dfs": 
    path, node_count, total_cost = dfs(graph, start_id, goal_ids)

  elif method == 'bfs':
    path, node_count, total_cost = bfs(graph, start_id, goal_ids)

  elif method == 'gbfs':
    path, node_count, total_cost = gbfs(graph, start_id, goal_ids)

  elif method == 'as':
    path, node_count, total_cost = astar_search(graph, start_id, goal_ids)

  elif method == 'cus1':
    path, node_count, total_cost = cus1(graph, start_id, goal_ids)

  elif method == 'cus2' or method == 'idas':
    path, node_count, total_cost = IDA_Star(graph, start_id, goal_ids)

  else:
    print("Unknown method!")
    return

  # Display result
  if not path:
    print(f"{filename} {method}")
    print("No solution")
    return

  goal = path[-1]

  print(f"{filename} {method}")
  print(f"{goal} {node_count} {total_cost}")
  print(" ".join(map(str, path)))


   
if __name__ == '__main__':
  main()
