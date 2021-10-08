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


def authorised(user_id):
    r = False
    if checkexist("authorised_users"):
        file = open("authorised_users")
        for line in file:
            if str(user_id) in line:
                r = True
                break
        file.close()
    return r


def getvalue(filename, userid):
    file = open(filename)
    value = ""
    for line in file:
        if str(userid) in line:
            for i in range(len(str(userid)) + 1, len(line)):
                value += line[i]
            break
    return value


def checkentryexists(filename, userid):
    exists = False
    file = open(filename)
    for line in file:
        if str(userid) in line:
            exists = True
            break
    return exists


def changevalue(filename, userid, newvalue):
    file = open(filename)
    createfile("temp_cv.txt")
    for line in file:
        if not str(userid) in line and not line.strip():
            appendfile(filename="temp_cv.txt", content=line)
    appendfile(
        filename="temp_cv.txt", content=str(userid) + ": " + str(newvalue) + "\n"
    )
    file.close()
    os.remove(filename)
    os.rename("temp_cv.txt", filename)
