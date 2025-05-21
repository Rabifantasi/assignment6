# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. 
# Show that it affects all instances.

class Bank:
    bank_name= "State Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name

    def display(self):
        print(f"Account Holder: {self.account_holder} , Bank Name: {Bank.bank_name}")

a= Bank("Rabia")
b= Bank("Farooq")

a.display()
b.display()

Bank.change_bank_name("National Bank")

a.display()     
b.display()

