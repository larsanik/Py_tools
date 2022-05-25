import os
print(os.environ["OS"])

from sys import platform, version, executable
print(platform)
print(version)
print(executable)
print("Hello, automation!")

import sys
print(sys.path)
help("modules")