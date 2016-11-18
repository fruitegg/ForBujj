class A:

    def __init__( self, p1 ):
        """ the constructor """
        self.p1 = p1

    def __repr__( self ):
        """ creates an appropriate string """
        s = self.p1
        return s

class B: 

    def __init__( self, p2 ):
        """ the constructor """
        p2 = self.p2

    def __repr__( self ):
        """ creates an appropriate string """
        s = self.p2
        return s 

a = A(42)
s = type(a).split('.')[-1]
print(s)

import os
def listFiles(path):
    if (os.path.isdir(path) == False):
        # base case:  not a folder, but a file, so return singleton list with its path
        return [path]
    else:
        # recursive case: it's a folder, return list of all paths
        files = [ ]
        for filename in os.listdir(path):
            files += listFiles(path + "/" + filename)
        return files

# To test this, download and expand this zip file in the same directory
# as the Python file you are running:  sampleFiles.zip

print(listFiles("sampleFiles"))
