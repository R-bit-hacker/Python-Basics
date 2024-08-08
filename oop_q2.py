class Account:
    def __init__(self,bal,acc):
        self.bal=bal
        self.acc=acc

    def debit(self,amount):
        self.bal-=amount
        print(f"Rs. {amount} was debited from your account")
        print("Total Balance= ", self.get_bal())

    def credit(self, amount):
        self.bal+=amount
        print(f"Rs. {amount} was credited to your account")
        print("Total Balance= ", self.get_bal())
    def get_bal(self):
        return self.bal
    
acc1= Account(10000, 1122)
acc1.debit(1000)
acc1.credit(500)