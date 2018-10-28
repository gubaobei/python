from random import randint
class Die():
    def __init__(self,sides=6):
        self.sides=sides
    def roll_die(self,number):
        for i in range(1,number+1):
            x=randint(1,self.sides)
            print('第'+str(i)+'次：',x)
die6=Die()
#die6.roll_die(10)
die10=Die(10)
#die10.roll_die(10)
die20=Die(20)
die20.roll_die(10)
