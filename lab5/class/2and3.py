class Shape:
    def area(self):
        return 0
    
class Sqaure(Shape):
    def __init__(self, length):
        self.length=length
    def area(self):
        print( self.length*self.length)


class Rectangle(Shape):
    def __init__(self,length,width) :
        self.length=length
        self.width= width
    def Area(self):
        print(self.length*self.width)
    


sh=Shape
sq=Sqaure
length=int(input())
print("square area is", end=' ')
sq.area(sq(length))
#print("area of rect is", end=" ")

r=Rectangle
w=int(input())
t=r(length,w)
print("area of rect is", end=" ")
r.Area(t)

#print(area)