class area:
    def _init_(self,a,b,c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
a= input("a=")
b= input("b=")
c= input("c=")

class triangle(area):
    def get_area(self):
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5

t = triangle(a,b,c)
print("area : {}".format(t.area()))