import os
import os.path as path
import re


for item in os.listdir("data"):
    print item

    # fix duplicate dots
    filename = "data/" + item
    new_filename = re.sub("\.+", ".", filename)
    os.rename(filename, new_filename)
    filename = new_filename

    # fix missing dots
    if filename[7] != ".":
        new_filename = "%s.%s" % (filename[:7], filename[7:])
        os.rename(filename, new_filename)
    else:
        pass
