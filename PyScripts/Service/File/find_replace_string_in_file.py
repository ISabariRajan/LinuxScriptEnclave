from os import environ
import sys

sys.path.append(environ["PYUTILS_PATH"])
from Utilities.package import GrepUtilities, join, pyScripPath

lines = ""
with open(join(pyScripPath, ".find"), "r") as f:
    lines = f.readlines()
find_string = " ".join(lines).replace("\n", "")

with open(join(pyScripPath, ".replace"), "r") as f:
    lines = f.readlines()
replace_string = " ".join(lines)
options = None
if len(sys.argv) > 2:
    options = sys.argv[2]

utils = GrepUtilities("TESTBOT")
utils.find_and_replace_line_in_file(find_string, replace_string, sys.argv[1], options=options)
