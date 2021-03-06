
# PercOS Utils

# Setup
import distutils.file_util as FUtil
import os

uFileName = "Users.prcdat"


# Function for decoring messages
def decor(st, m):
    nhastag = 40
    msg = ("\n" * m) + ("#" * (nhastag + 23)) + "\n" + st + "\n"
    msg = msg + ("#" * (nhastag + 23)) + "\n"
    return msg


# Init Message
def printInit():
    version = "Alpha 1.1.0"
    print(decor("PercOS Utils " + version, 1))


# Advanced input functions
def getProbedInput(prompt, accepted, default=None):
    while True:
        value = input(prompt).lower()

        if value in accepted:
            return value
        elif default is not None and value == '':
            return default
        else:
            print(value + ' is not a valid response')


def getProbedInputNormal(prompt, accepted):
    while True:
        value = input(prompt)

        if value in accepted:
            return value
        else:
            print(value + ' is not a valid response')


# Function for writing to the users.prc file
def writeUsers(users, pases, superusers):
    f = open(uFileName, 'w')
    for user in users:
        i = users.index(user)
        pas = pases[i]
        perm = '0'
        if user in superusers:
            perm = '1'
        f.write(user + ',' + pas + ',' + perm + '\n')
    f.close()


# function for making and writing files
def mkFile(filename):
    lines = []
    while True:
        line = input(' ')
        if line == '\\':
            break
        else:
            lines.append(line)
    FUtil.write_file(filename, lines)


def concat(list):
    r = ""
    for s in list:
        r += s
    return r


def concatDirs(list):
    r = ""
    for s in list:
        r += s + "/"
    return r


def dirdow(dir):
    # print('dir:', dir)
    ls = dir.split("/")
    # ls.remove("")
    ls.pop()
    r = concatDirs(ls)
    # print('r:', type(r))
    r = r.rstrip('/')
    return r


class Dire:

    def __init__(self, baseDir, usersDir, user):
        self.dir = "/" + usersDir + "/" + user
        self.realdir = os.getcwd() + "/" + baseDir + self.dir
        self.bd = baseDir

    def cd(self, toGo, simbolic):
        if simbolic:
            r = Dire('', '', '')
            r.bd = self.bd
            r.realdir = self.realdir
            r.dir = self.dir

            if ".." in toGo:
                if toGo.startswith("/"):
                    print("Can't go lower than the base directory.")
                else:
                    levdow = toGo.split("/").count("..")
                    i = 0
                    while i < levdow:
                        i += 1
                        r.dir = dirdow(r.dir)
                    r.realdir = os.getcwd() + "/" + r.bd + r.dir

            else:
                if toGo.startswith("/"):
                    r.dir = toGo
                    r.realdir = os.getcwd() + "/" + r.bd + r.dir
                else:
                    r.dir = r.dir + "/" + toGo
                    r.realdir = os.getcwd() + "/" + r.bd + r.dir
            return r
        else:
            if ".." in toGo:
                if toGo.startswith("/"):
                    print("Can't go lower than the base directory.")
                else:
                    levdow = toGo.split("/").count("..")
                    i = 0
                    while i < levdow:
                        i += 1
                        self.dir = dirdow(self.dir)
                    self.realdir = os.getcwd() + "/" + self.bd + self.dir

            else:
                if toGo.startswith("/"):
                    self.dir = toGo
                    self.realdir = os.getcwd() + "/" + self.bd + self.dir
                else:
                    self.dir = self.dir + "/" + toGo
                    self.realdir = os.getcwd() + "/" + self.bd + self.dir
