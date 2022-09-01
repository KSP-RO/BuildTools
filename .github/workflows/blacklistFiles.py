import argparse
import os
parser = argparse.ArgumentParser("test")
parser.add_argument('workspace', metavar='workspace', type=str,
                   help='workspace path')
parser.add_argument('path', metavar='path', type=str,
                   help='path to blacklist file')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--enable', action='store_true')
group.add_argument('--disable', action='store_true')

args = parser.parse_args()


# Either 'enable' or 'disable'. checking if enable is enough
enable = args.enable
workspace = args.workspace
path = args.path

# TODO: make sure correct nr of '/' are used in path merge
def merge_paths(workspace, path):
    return workspace + "/" + path

print(f"output: path: {path}, enable: {enable}")

with open(path, 'r') as f:
    files = f.readlines()

for file in files:
    new_name = name = merge_paths(workspace, file)
    # if we want to disable the file, we add '.disabled', if we want to enable we remove '.disabled'
    if enable:
        name += ".disabled"
    else:
        new_name += ".disabled"

    print(f"Renaming file {name} to {new_name}")
    os.rename(name, new_name)
