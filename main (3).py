class Bank_Account:
    def __intit__(self) :
        self.balance=0
        print("Hello!!! Welcome to the Deposite & Withdrawal Machine")

    def deposit (self):
         amount=float(input("Enter amount to be Deposited: ")) 
         self. balance +=amount
         print("\n Amount Deposited:",amount)

    def withdraw(self):
        amount = float(input(" Enter amount to be withdrawn:"))
        if self.balance>=amount:
           self.balance>=amount
           print("\n You Withdrew:",amount) 
        else:
           print("\n Insufficient balance")

    def display(self):
        print("\n Net Available Balance=",self.balance)
                  