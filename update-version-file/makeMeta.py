import os, argparse, sys, json, glob, re

class DefaultHelpParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

HELP_DESC = "Creates neccesary metadata files"
parser = DefaultHelpParser(description=HELP_DESC)
parser.add_argument('tag', metavar='tag', type=str, nargs=1,
                   help='tag of release (e.g. 0.4.6.0')
parser.add_argument('path', metavar='path', type=str, nargs=1,
                   help='path to version file')

args = parser.parse_args()

if not args.tag or len(args.tag) < 1:
    print("ERROR: git tag must be specified and must be in the format major.minor.patch.build-configuration.e.g. 0.4.6.0")
    sys.exit(2)
if not args.path or len(args.path) < 1:
    print("ERROR: version file path must be specified")
    sys.exit(2)

version = args.tag[0]
path = args.path[0]

if version.startswith('v'):
    version = version.split('v')[1]

major = int(version.split(".")[0])
minor = int(version.split(".")[1])
patch = int(version.split(".")[2])
build = int(version.split(".")[3])
# regex replace in AVC .version file
new_version = []
in_version = False
with open(path, "r") as f:
    for line in f.readlines():
        # Replace version in links
        line = re.sub(r"v\d+.\d+.\d+.\d+", f"v{major}.{minor}.{patch}.{build}", line)
        if "\"VERSION\": {" in line:
            in_version = True
        if "}" in line:
            in_version = False
        if in_version:
            # Replace version in version node
            line = re.sub(r"\"MAJOR\":\s\d+", f"\"MAJOR\": {major}", line)
            line = re.sub(r"\"MINOR\":\s\d+", f"\"MINOR\": {minor}", line)
            line = re.sub(r"\"PATCH\":\s\d+", f"\"PATCH\": {patch}", line)
            line = re.sub(r"\"BUILD\":\s\d+", f"\"BUILD\": {build}", line)
        new_version.append(line)

with open(path, "w") as f:
    f.writelines(new_version)
