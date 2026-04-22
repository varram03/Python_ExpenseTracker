import matplotlib.pyplot as plt
from analytics import categoricalExpense, monthlyExpense, categoryShare

def categoryChart():
    data = categoricalExpense()
    data.plot(kind = 'bar')
    plt.title("Expense by category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()

def monthlygraph():
    data = monthlyExpense()
    data.plot(kind = 'line', marker = 'o')
    plt.title("Monthly Expenses")
    plt.xlabel("Monthly")
    plt.ylabel("Amount")
    plt.show()

def piechart():
    data = categoryShare()
    data.plot(kind = 'pie',autopct = '%1.1f%%')
    plt.title("Expense Distribution")
    plt.ylabel("")
    plt.show()


