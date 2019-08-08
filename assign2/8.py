x=raw_input()
import os
words=x.split("/")
print words[-1]
print os.path.dirname(x)
print os.path.abspath(x)
print os.path.basename(x)
