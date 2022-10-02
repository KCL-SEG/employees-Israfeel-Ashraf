"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from Contract import Contract
from Commission import *

class Employee:
    
    def __init__(self, name, contract, commission):
        
        self.name = name
        self.contract = contract
        self.commission = commission
        
    def get_pay(self):
        
        return self.contract.get_contract_payment() + self.commission.calculate_commission()

    def __str__(self):

        contract_String = self.contract.get_Salary_Type()

        amount_string = self.contract.get_String()

        if self.commission.commission_type == "None": cString = ""
        elif self.commission.commission_type == "Bonus": cString = " and receives a bonus commission of {0}".format(self.commission.amount)
        else: cString = " and receives a commission for {0} contract(s) at {1}/contract".format(self.commission.number_of_contracts, self.commission.amount)

        return "{0} works on a {1} of {2}{3}.  Their total pay is {4}.".format(self.name, contract_String, amount_string, cString, self.get_pay())



billie_contract = Contract("monthly", 4000)

charlie_contract = Contract("hourly", 25, 100)

renee_contract = Contract("monthly", 3000)

jan_contract = Contract("hourly", 25, 150)

robbie_contract = Contract("monthly", 2000)

ariel_contract = Contract("hourly", 30, 120)



billie_commission = Commission("None", 0, 0)

charlie_commission = Commission("None", 0, 0)

renee_commission = Commission("Contract-dependent", 200, 4)

jan_commission = Commission("Contract-dependent", 220, 3)

robbie_commission = Commission("Bonus", 1500, 1)

ariel_commission = Commission("Bonus", 600, 1)


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', billie_contract, billie_commission)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', charlie_contract, charlie_commission)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', renee_contract, renee_commission)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', jan_contract, jan_commission)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', robbie_contract, robbie_commission)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', ariel_contract, ariel_commission)
