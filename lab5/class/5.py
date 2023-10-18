class account:
    def __init__(self,name, balance=0):
        self.name=name
        self.balance=balance
    def plus(self,add):
        self.add=self.balance+add 
        print("Tvoi balance" ,self.name,": ", self.add)
    def proverka(self,min):
        self.min=min
        if min>self.balance:
            print("money money jetpeidy")
        else:
            self.balance=self.add-min
            print("balance bar",self.name," :", self.balance)


b=account('Aisha',900)
b.plus(2500)
b.proverka(4500)

d=account('Dan',5000)
d.plus(12000)
d.proverka(3000)
d.proverka(50000)