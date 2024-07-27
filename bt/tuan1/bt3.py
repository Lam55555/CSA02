from datetime import datetime
today =  datetime.today()
class CustomDate:
    # def __init__(self):
        # self = self
    def datet(self):
        print(today.strftime('%d/%m/%Y'))
    def  timet(self):
        print(today.strftime('%H:%M:%S'))
now = CustomDate()
now.datet()
now.timet()