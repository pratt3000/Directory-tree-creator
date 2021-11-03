
# Problem Statement :
Come up with a config (Data Structure) and load a new directory tree from config.
Write a program that does flowing operations on a directory tree.
Add a new folder at a particular path in the directory tree.
Removed a folder from a particular path in the directory tree.
Fetch the path of the given folder.
Update name of the folder.

Note: For each folder we should have unique `id` and `name`.
Also upload the program on github and share the link with README.

## Dependencies
1. `pip install pprint`
2. `pip install uuid`

## To run
1. python main.py

## Options while running
1. Add node -> Add a new node to the data structure bu specifying its immediate parent node and new node name
2. Delete node -> Enter name of node to be deleted (All of its children are deleted too)
3. Rename node -> specify new and old name for a node and it gets renamed
4. Fetch node path -> Beginning from the root node the full path of the node is printed
5. Print tree -> the tree structure is printed
0. EXIT > exit program

## Edge cases

### Method_01
Used multiple data structures to maintain all info.
Edge case 1 - All folders must be uniquely named <br>
soln - could change the whole structure to nested dicts

### Method_02
Used a single more elegant data structure/
Assumption - currently printing the first folder which is found in tree, for the fetch method.
Alternatives:
1. Pass id along ith name and find the specific folder.
2. Find all foler having that name instead of the first.



