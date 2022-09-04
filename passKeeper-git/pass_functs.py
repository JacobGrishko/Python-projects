import pass_crypt


'''
PassSet class describes a data structure of a set
A set is an object that holds a platform name, username and user password together
1.init creates a set
2.sets getters
3.repr returns a representation of a set
4.str return the set as a string
'''
class PassSet:
    def __init__(self, platf, uname, upass):
        self.plat = platf
        self.name = uname
        self.pssw = upass

    def getPlat(self):
        return self.plat
    def getName(self):
        return self.name
    def getPass(self):
        return self.pssw

    def __repr__(self):
        return "{"+self.plat+":"+self.name+":"+self.pssw+"}"
        # return self.plat + " - " + self.name + " - " + self.pssw

    def __str__(self):
        return self.plat + " - " + self.name + " - " + self.pssw
        # return "{" + self.plat + ":" + self.name + ":" + self.pssw + "}"

