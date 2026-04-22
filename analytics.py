from storage import loadData
import pandas as pd

def totalExpense():
    df = loadData()
    df.columns = df.columns.str.strip().str.lower()
    total = df['amount'].sum()
    return total

def categoricalExpense():
    df = loadData()
    df.columns = df.columns.str.strip().str.lower()
    total = df.groupby('category')['amount'].sum()
    return total

def monthlyExpense():
    df = loadData()
    df.columns = df.columns.str.strip().str.lower()
    if df.empty:
        return {}
    df['date'] = pd.to_datetime(df['date'], format = "%d-%m-%Y")
    total = df.groupby(df['date'].dt.to_period('M'))['amount'].sum()
    return total

def highestCategory():
    res = categoricalExpense()
    return res.idxmax()

def highestMonth():
    res = monthlyExpense()
    return res.idxmax()

def avgExp():
    df = loadData()
    return df['amount'].mean()

def totTransactions():
    df = loadData()
    return len(df)

def categoryShare():
    res = categoricalExpense()
    if res.sum()==0:
        return res
    pc = (res/res.sum()) * 100
    return pc

def recentTransactions(n):
    df = loadData()
    if df.empty:
        return df
    return df.tail(n)
