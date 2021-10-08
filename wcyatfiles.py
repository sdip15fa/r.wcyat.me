import os
from os.path import exists

def createfile(filename):
    if checkexist(filename):
        os.remove(filename)
    fp = open(filename, "w")
    fp.close()


def checkexist(filename):
    r = bool(exists(filename))
    return r


def appendfile(filename, content):
    if checkexist(filename):
        fp = open(filename, "a")
        fp.write(content)
        fp.close()
    else:
        fp = open(filename, "w")
        fp.write(content)
        fp.close()