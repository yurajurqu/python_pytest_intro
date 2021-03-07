
import os
def readFromFile(filename):
    if not os.path.exists(filename):
        raise Exception('Bad file')
    f = open(filename, "r")
    return f.readLine()