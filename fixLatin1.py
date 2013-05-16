import os
import csv


# access each file and convet contents to utf-8
"""
for f in os.listdir("data"):
    fname="data/" + f
    with open(fname, "r") as fp:
        contents = fp.read()
    contents = contents.decode("latin1")
    contents = contents.encode("utf8")
    with open(fname, "w+") as fp:
        fp.write(contents)
        """
