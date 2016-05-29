#利用面向对象继承机制，定义椭圆（Ellipse）、正方形（Square）、矩形（Rectangle）、圆形（Circle）等类
#设计一个函数compute_area（shapes），输入一个圆形列表，输出这些圆形的面积之和
#shapes＝[Ellipse(10,20),Square(15),Circle(5),Rectangle(20,15),Circle(5),Square(15),Ellipse(10,20)]
#total_area=compute_area(shapes)
#print(total_area)

from math import pi
import logging

class shape():
    def __init__(self):
        pass

    def say(self):
        print(self.__class__.__name__)

    def compute_area(self):
        pass

    def say_area(self):
        print("%s 's area is: %f" % (self.__class__.__name__, self.compute_area()))

class Ellipse(shape):
    def __init__(self,major_axis, minor_axis):
        super(Ellipse, self).__init__()
        self.a=major_axis
        self.b=minor_axis

    def compute_area(self):
        return self.a*self.b*pi


class Square(shape):
    def __init__(self,side):
        super(Square, self).__init__()
        self.a=side
        
    def compute_area(self):
       return self.a*self.a


class Rectangle(shape):
    def __init__(self, length, width):
        super(Rectangle,self).__init__()
        self.a = length
        self.b = width

    def compute_area(self):
        return self.a*self.b


class Circle(shape):
    def __init__(self, radius):
        super(Circle, self).__init__()
        self.r = radius

    def compute_area(self):
        return pi*(self.r*self.r)        
def main():
    Es = Ellipse(10,20)
    Es.say_area()
    Sq = Square(15)
    Sq.say_area()
    Cr = Circle(5)
    Cr.say_area()
    Re = Rectangle(20,15)
    Re.say_area()
    Cr = Circle(5)
    Cr.say_area()
    Sq = Square(15)
    Sq.say_area()
    Es = Ellipse(10,20)
    Es.say_area()
    shapes=[Es.compute_area(),Sq.compute_area(),Cr.compute_area(),Re.compute_area(),Cr.compute_area(),Sq.compute_area(),Es.compute_area()]             

    def compute_area(shapes):
        sum=0.0
        for i in range(len(shapes)):
            sum += shapes[i]
        return sum
    total_area=compute_area(shapes)
    print('以上所有图形面积之和为：',total_area)
    
if __name__ == '__main__':
    main()
   

 
   

