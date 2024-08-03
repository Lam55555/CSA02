class MathList:
    def __init__(self, values):
        self.values = values
    
    def __str__(self):
        return str(self.values)
    
    def __add__(self, number):
        return [x + number for x in self.values]
    
    def __sub__(self, number):
        return [x - number for x in self.values]

m_list= MathList([1, 2, 3, 4, 5])
print(m_list)
m_list += 2
print(m_list)
