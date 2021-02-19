from . import Expense

class BudgetList(self,budget):
    self.budget = budget
    self.sum_expenses = 0
    self.expenses = []
    self.sum_overages = 0
    self.overgaes = []

    def append(self, item):
        if self.sum_expenses+item<self.budget:
            self.expenses.append(item)
            self.sum_expenses+=item
        else: 
            self.overages.append(item)
            self.sum_overages+=item

    def __len__(self):
        return self.expenses.len()+self.overages.len()

    
def main():
    myBudgetList = BudgetList(1200)
if __name__ is "__main__":
    main()

expenses = Expense.Expenses()
expenses.read_expenses("data/spending_data.csv")

for expense in expenses.list:
    myBudgetList.append(expense.amount)

print('The count of all expenses: ' + str(myBudgetList.len()))




    
            

