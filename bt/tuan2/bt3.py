class Square:
    def __init__(self,cdc):
        self.cdc = cdc

    def cal_area(self):
        return self.cdc * self.cdc
class Cube(Square):
    def cal_area(self):
        return self.cdc * self.cdc * 6
    
    def cal_volume(self):
        return self.cdc * self.cdc * self.cdc
    
square = Square(2)
print('Square area:', square.cal_area())
cube = Cube(2)
print('Cube area:', cube.cal_area())
print('Cube volume:', cube.cal_volume())
