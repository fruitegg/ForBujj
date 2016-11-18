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
