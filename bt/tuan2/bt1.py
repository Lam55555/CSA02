class Rectangle:
    def __init__(self,h,w):
        self.w = w
        self.h = h

    def __str__(self):
        return f'Rectangle object with height = {self.h} and width = {self.w}'
    
rect = Rectangle(2,1)
print(rect)