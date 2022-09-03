import argparse
import os
parser = argparse.ArgumentParser("test")
parser.add_argument('workspace', metavar='workspace', type=str,
                   help='workspace path')
parser.add_argument('path', metavar='path', type=str,
                   help='path to blacklist file')

args = parser.parse_args()


# Either 'enable' or 'disable'. checking if enable is enough
workspace = args.workspace
path = args.path

# TODO: make sure correct nr of '/' are used in path merge
def merge_paths(workspace, path):
    return workspace + "/" + path

with open(path, 'r') as f:
    files = f.readlines()

for file in files:
    new_name = name = merge_paths(workspace, file)
    # Add '.disabled' to file names
    name += ".disabled"

    print(f"Renaming file {name} to {new_name}")
    os.rename(name, new_name)
