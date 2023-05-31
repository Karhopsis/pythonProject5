class TriangleChecker():
    def __init__(self,a,b,c):
            self.a = a
            self.b = b
            self.c = c

    def is_triangle(self):
        if self.a<0 or self.b<0 or self.c<0:
            return "negative number"
        else:
            if self.a+self.b>self.c and self.b+self.c>self.a and self.c+self.a>self.b:
                return "your triangle is possible"
            else:
                return "your triangle is not possible"



trChecker = TriangleChecker((-4),5,8)
print(trChecker.is_triangle())



