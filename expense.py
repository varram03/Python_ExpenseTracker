class Expense:
    def __init__ (self,date,category,amt,desc):
        self.date = date
        self.category = category
        self.amt = amt
        self.desc = desc
    
    def to_List(self):
        return [self.date,self.category, self.amt, self.desc]