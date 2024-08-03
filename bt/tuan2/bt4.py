from datetime import datetime as dt
class User:
    def __init__(self,username, password):
        self.usn = username
        self.pas = password

    def welcome(self):
        print(f'Welcome, {self.usn}')
    
    def check_password(self, ckpass):
        return self.pas == ckpass

class SubscribedUser(User):
    def __init__(self, username, password, nhh):
        super().__init__(username, password)
        self.nhh = nhh
    
    def is_expired(self):
        now = dt.now()
        now.strftime("%d/%m/%Y")
        return now > self.nhh
    
user = User('mindx', '12345')
user.welcome()
print(user.check_password('1234'))
s_user = SubscribedUser('s_mindx', '1234', dt(2021, 1, 1))
s_user.welcome()
print(s_user.check_password('1234'))
print(s_user.is_expired())
