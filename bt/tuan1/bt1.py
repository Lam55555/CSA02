class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def say_hi(self):
        print(f'Hi, my name is {self.name}')
    def tell_position(self):
        print(f'I am a {self.position}')
john = Employee('John', 'Software Engineer')
john.say_hi()
john.tell_position()
