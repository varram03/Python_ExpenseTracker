import csv
import pandas as pd
import os 

def saveData(expense):
    file_exist = os.path.isfile("Expenses.csv")
    f = open("Expenses.csv", mode = 'a', newline = "")
    writer = csv.writer(f)
    if not file_exist:
        writer.writerow(["date","category","amount","description"])
    writer.writerow(expense.to_List())
    f.close()

def loadData():
    df = pd.read_csv("Expenses.csv")
    return df