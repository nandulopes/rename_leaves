#!/usr/bin/env python

####Description: rename tips of newick tree files
####dictionary_filename: a csv semi-colon delimited file. First column current tips names; second column new tips names
####Use: python rename_leaves.py ; then type the name of your dictionary (csv)
####     and after that type the name of your newick file
####Written by: Fernando Lopes - nandulopes@gmail.com



from ete3 import Tree
import csv

# Prompt the user to input the name of the dictionary file
dictionary_filename = input("Please enter the name of the dictionary file: ")

# Read the dictionary from the CSV file
name_dict = {}
with open(dictionary_filename) as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        name_dict[row[0]] = row[1]

# Prompt the user to input the name of the tree file
tree_filename = input("Please enter the name of the tree file: ")

# Read the Newick tree from the file
with open(tree_filename) as f:
    newick_tree = f.readline().strip()

# Define a function to map node names to the desired values using the dictionary
def map_names(node):
    if node.name in name_dict:
        node.name = name_dict[node.name]

# Read the tree from the Newick format string
t = Tree(newick_tree)

# Map node names to the desired values using the dictionary
for node in t.traverse():
    map_names(node)

# Traverse the tree again and map the names of internal nodes
for node in t.traverse("postorder"):
    if not node.is_leaf():
        node.name = ""

    if node.up is not None and node.up.name != "":
        node.name = name_dict.get(node.up.name, "")

# Save the modified tree with the name of the tree file followed by "_fullnames"
output_filename = tree_filename.split(".")[0] + "_fullnames.tree"
t.write(outfile=output_filename)

# Print a message indicating where the output was saved
print(f"Output saved as {output_filename}")
