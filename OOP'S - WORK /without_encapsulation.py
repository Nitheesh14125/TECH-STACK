class bankaccount:
    def __init__(self,balance):
        self.balance = balance 


acc = bankaccount(1500)
print(acc.balance)

acc.balance = acc.balance + 500 

print(acc.balance)

#without any deposit or withdrawal method we have made the change in the account balance which is not an secure way of working 

