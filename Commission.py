
class Commission:

    def __init__(self, commission_type, amount, number_of_contracts):
        self.commission_type  = commission_type
        self.amount = amount
        self.number_of_contracts = number_of_contracts

    def get_commission_type(self):
        return self.commission_type


    def calculate_commission(self):

        if self.number_of_contracts > 1:
            return self.number_of_contracts * self.amount


        else:
            return self.amount
            
        
#billie_commission = Commission("Non-fixed", 200, 4)
#print(billie_commission.calculate_commission())
