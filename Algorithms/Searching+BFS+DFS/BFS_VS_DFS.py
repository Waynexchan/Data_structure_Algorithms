# //If you know a solution is not far from the root of the tree:

use BFS, because it is the shortest path to access the node
# //If the tree is very deep and solutions are rare: 
use BFS, because it spends a lot of time to traversal the deep path by using DFS

# //If the tree is very wide:
use DFS, because BFS will consume a lot of memory to save the pointer in each level if we use BFS

# //If solutions are frequent but located deep in the tree:
USE DFS because we know that it is in the deeply location. it can save memory when compare with using BFS method

# //Determining whether a path exists between two nodes:
use DFS

# //Finding the shortest path:
BFS, because it can find the shortest path to find the answer