import argparse, sys, re

class DefaultHelpParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

HELP_DESC = "Replaces version string in readme"
parser = DefaultHelpParser(description=HELP_DESC)
parser.add_argument('tag', metavar='tag', type=str, nargs=1,
                   help='tag of release (e.g. 0.4.6.0')
parser.add_argument('path', metavar='path', type=str, nargs=1,
                   help='path to readme')

args = parser.parse_args()

if not args.tag or len(args.tag) < 1:
    print("ERROR: git tag must be specified and must be in the format major.minor.patch.build-configuration.e.g. 0.4.6.0")
    sys.exit(2)
if not args.path or len(args.path) < 1:
    print("ERROR: Readme path must be specified")
    sys.exit(2)

version = args.tag[0]
path = args.path[0]

if version.startswith('v'):
    version = version.split('v')[1]

# Replace old version tag in readme
new_string = "compare/v"+version+"...master"
new_readme = []
with open(path, "r") as f:
    for line in f.readlines():
        replaced = re.sub(r'compare/v[\d|.]*...master', new_string, line)
        new_readme.append(replaced)

with open(path, "w") as f:
    f.writelines(new_readme)
