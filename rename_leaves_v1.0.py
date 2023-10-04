#!/usr/bin/env python

####Description: rename tips of newick tree files
####dictionary_filename: a csv semi-colon delimited file. First column current tips names; second column new tips names
####Use: python rename_leaves_v1.0.py ; then type the name of your dictionary (csv) ; then the name of your output with extension
####     and after that type the name of your newick file
####Written by: Fernando Lopes - nandulopes@gmail.com

from ete3 import Tree
import csv
import os

# Prompt the user to input the name of the dictionary file
dictionary_filename = input("Please enter the name of the dictionary file: ")

# Validate that the dictionary file exists
if not os.path.isfile(dictionary_filename):
    print(f"Dictionary file '{dictionary_filename}' does not exist.")
    exit(1)

# Read the dictionary from the CSV file
name_dict = {}
with open(dictionary_filename) as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        name_dict[row[0]] = row[1]

# Prompt the user to input the name of the tree file
tree_filename = input("Please enter the name of the tree file: ")

# Validate that the tree file exists
if not os.path.isfile(tree_filename):
    print(f"Tree file '{tree_filename}' does not exist.")
    exit(1)

# Read the Newick tree from the file, handling multiline Newick format
with open(tree_filename) as f:
    lines = f.readlines()
    newick_tree = "".join([line.strip() for line in lines])

# Define a function to map node names to the desired values using the dictionary
def map_names(node):
    node.name = name_dict.get(node.name, node.name)

# Read the tree from the Newick format string
t = Tree(newick_tree, format=1)

# Map node names to the desired values using the dictionary
for node in t.traverse():
    map_names(node)

# Prompt the user to input the name of the output file with extension
output_filename = input("Please enter the name of the output file (with extension): ")

# Save the modified tree with the specified output filename
t.write(outfile=output_filename, format=1)

# Print a message indicating where the output was saved
print(f"Output saved as {output_filename}")
