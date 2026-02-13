import sys
from parser import parse_problem_file
from algorithms.cus2 import IDA_Star

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

  #
  path = []
  node_count = 0
  total_cost = 0

  # Solve and return the result
  if method == "dfs": 
    pass
  elif method == 'bfs':
    pass    
  elif method == 'gbfs':
    pass    
  elif method == 'as':
    pass    
  elif method == 'cus1':
    pass    
  elif method == 'cus2' or method == 'idas':
    path, node_count, total_cost = IDA_Star(graph, start_id, goal_ids)

  # Display result
  if not path:
    print(f"{filename} {method}")
    print("No solution")
    return

  goal = path[-1]

  print(f"{filename} {method}")
  print(f"{goal} {node_count}")
  print(" ".join(map(str, path)))

   
if __name__ == '__main__':
  main()