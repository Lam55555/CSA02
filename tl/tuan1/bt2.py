# l = int(input("Enter the length of the rectangle: "))
# w = int(input("Enter the width of the rectangle: "))
class Rectangle:
    def __init__(self, chieudai, chieurong):
        self.chieudai = chieudai
        self.chieurong = chieurong
    def dientich(self):
        kq = self.chieudai * self.chieurong
        print(kq)
    def chuvi(self):
        kq = (self.chieudai + self.chieurong)*2
rec1 = Rectangle(4,6)
rec1.dientich()


# l = int(input("Enter the length of the rectangle: "))
# w = int(input("Enter the width of the rectangle: "))

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length      
#         self.width = width

#     def calcPerimeter(self):
#         answer = 2 * (self.length + self.width)
#         print(answer)
    
#     def calcArea(self):
#         answer = self.width * self.length 
#         print(answer)
    
# rec1 = Rectangle(5, 4)
# rec1.calcPerimeter()
# rec1.calcArea()