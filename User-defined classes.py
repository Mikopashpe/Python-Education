'''
В данном файле идет ознакомление с классами
'''

class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split() [-1]
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
        
Johnn = Worker('Johnn Brown', 2000)
Billy = Worker('Billy Idol', 20000)
print(Johnn.lastName())

Billy.giveRaise(.30)
print(Billy.pay)