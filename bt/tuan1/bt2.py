class Hinh:
    def __init__(self,w,h,r):
        self.w = w
        self.h = h
        self.r = r
    def hcn(self):
        p = (self.w + self.h)*2
        s = self.w*self.h
        print(f'Perimeter: {p}')
        print(f'Area: {s}')
    def ht(self):
        p = 2*3.14*self.r
        s = self.r*self.r*3.14
        print(f'Perimeter: {p}')
        print(f'Area: {s}')
shape = str(input('Shape (rectangle | circle):\n'))
if shape == 'rectangle':
    w = int(input('Width: '))
    h = int(input('Height: '))
    chuvihcn = Hinh(w,h,None)
    chuvihcn.hcn()
elif shape == 'circle':
    r = int(input('Radius: '))
    hinhtron = Hinh(None, None, r)
    hinhtron.ht()