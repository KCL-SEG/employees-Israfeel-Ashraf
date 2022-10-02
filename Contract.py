

class Contract:

    def __init__(self, salary_Type, *args):
        self.salary_Type = salary_Type

        if len(args) == 2:
            self.amount = args[0]
            self.hours = args[1]

        else:
            self.amount = args[0]

        
    def get_Salary_Type(self):

        if self.salary_Type == "monthly":
            return "monthly salary"

        elif self.salary_Type == "hourly":
            return "contract"

        else:
            return None

    def get_String(self):
        try:
            return "{0} hours at {1}/hour".format(self.hours, self.amount)

        except AttributeError:
            return "{0}".format(self.amount)
        

    def get_contract_payment(self):

        try:
            return self.hours * self.amount

        except AttributeError:
            return self.amount


