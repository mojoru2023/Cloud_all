import os
import sys
import json

def tree_path_json(path):
    dir_structure = {}
    base_name = os.path.basename(os.path.realpath(path))
    if os.path.isdir(path):
        dir_structure[base_name] = [ tree_path_json(os.path.join(path, file_name))\
         for file_name in os.listdir(path) ]
    else:
        return os.path.basename(path)
    return dir_structure


print(tree_path_json("/home"))
