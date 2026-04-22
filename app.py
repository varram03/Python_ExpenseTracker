from expense import Expense
from storage import saveData
from datetime import datetime
from analytics import totalExpense, highestCategory, highestMonth, avgExp, recentTransactions
from charts import categoryChart, monthlygraph, piechart
import tkinter as tk;
from tkinter import ttk, messagebox;

from datetime import datetime
def validateDate(date):
    try:
        datetime.strptime(date, "%d-%m-%Y")
        return True
    except ValueError:
        return False

def save_expense():
    date = date_entry.get()
    category = category_var.get()
    amount = amount_entry.get()
    desc = desc_entry.get()

    if category=="Other":
        category = other_entry.get()
    
    if not validateDate(date):
        messagebox.showerror("Invalid date", 
        "Enter date in DD-MM-YYYY format")
        return
    
    if category.strip()=="":
        messagebox.showerror("Invalid Category", 
        "Category cannot be empty"
        )
        return
    
    try:
        amount = float(amount)
        if amount<=0:
            raise ValueError
    except ValueError:
        messagebox.showerror(
            "Invalid Amount",
            "Enter a positive number"
        )
        return
    
    exp = Expense(date, category, amount, desc)
    saveData(exp)

    messagebox.showinfo("Success!", "Expense added successfully!")
    clear_fields()

def clear_fields():
    date_entry.delete(0,tk.END)
    amount_entry.delete(0,tk.END)
    desc_entry.delete(0,tk.END)
    other_entry.delete(0,tk.END)
    other_entry.pack_forget()
    category_var.set(categories[0])

def open_dashboard():
    dash = tk.Toplevel(root)
    dash.title("Dashboards")
    dash.geometry("500x500")
    dash.configure(bg = "#eef2f3")

    tk.Label(
        dash,
        text = "Expense Dashboard",
        font = ("Times New Roman", 20, "bold"),
        bg = "#eef2f3",
        fg = "#000000"
    ).pack(pady=15)

    box = tk.Frame(
        dash,
        bg = "white",
        padx = 25,
        pady = 25,
        bd = 2,
        relief = "groove"
    )
    box.pack(pady = 15)

    tk.Label(
        box,
        text = f"Total Expense: {totalExpense()}",
        font = ("Times New Roman", 12),
        bg ="white",
    ).pack(pady=6)

    tk.Label(
        box,
        text = f"Highest Expense Category: {highestCategory()}",
        font = ("Times New Roman", 12),
        bg ="white",
    ).pack(pady=6)

    tk.Label(
        box,
        text = f"Highest Spending Month: {highestMonth()}",
        font = ("Times New Roman", 12),
        bg ="white",
    ).pack(pady=6)

    tk.Label(
        box,
        text = f"Average Expense: {avgExp()}",
        font = ("Times New Roman", 12),
        bg ="white",
    ).pack(pady=6)

    tk.Label(
        dash,
        text = "Recent Expenses",
        font = ("Times New Roman", 20, "bold"),
        bg = "#eef2f3"
    ).pack(pady = 10)

    table_frame = tk.Frame(dash)
    table_frame.pack(pady=5)
    columns = ("Date", "Category", "Amount", "Description")
    tree = ttk.Treeview(
        table_frame, 
        columns = columns, 
        show = "headings",
        height = 5
    )
    for col in columns:
        tree.heading(col, text = col)
        tree.column(col,width = 100)
    tree.pack()
    recent = recentTransactions(5)
    for _, row in recent.iterrows():
        tree.insert(
            "",
            tk.END,
            values=(
                row["date"],
                row["category"],
                row["amount"],
                row["description"]
            )
        )

    tk.Label(
        dash,
        text = "Charts",
        font = ("Times New Roman", 20,"bold"),
        bg ="#eef2f3",
    ).pack(pady=10)

    tk.Button(
        dash,
        text = f"Category Chart",
        command = categoryChart,
        width = 18,
        bg = "#3498db",
        fg = "white"
    ).pack(pady = 6)

    tk.Button(
        dash,
        text = "Monthly Trend",
        command = monthlygraph,
        width = 18,
        bg = "#3498db",
        fg = "white"
    ).pack(pady = 6)

    tk.Button(
        dash,
        text = "Expense Pie Chart",
        command = piechart,
        width = 18,
        bg = "#3498db",
        fg = "white"
    ).pack(pady = 6)

def show_other(event):
    if category_var.get()=="Other":
        other_entry.pack(after = dropdown, pady=6)
    else:
        other_entry.pack_forget()

""" GUI """
root = tk.Tk()
root.title("Personal Expense Tracker")
root.geometry("430x520")
root.configure(bg = "#eef2f3")

title = tk.Label(root, text = "Expense Tracker", font=("Times New Roman", 22, "bold", "italic"),
                bg = "#eef2f3", fg = "#000000")
title.pack(pady = 20)
card = tk.Frame(root, bg="white", padx = 30, pady = 30, bd = 2, relief = "groove")
card.pack()

tk.Label(card, text = "Date (DD-MM-YYYY)", bg = "white").pack()
date_entry = tk.Entry(card, width=30)
date_entry.pack(pady=8)
categories = ["Food", "Transport", "Entertainment", "Shopping", "Utilities", "Health", "Other"]
category_var = tk.StringVar()
category_var.set(categories[0])
dropdown = ttk.Combobox(
    card, 
    textvariable = category_var, 
    values=categories, 
    state="readonly", 
    width = 27
)
dropdown.pack(pady=8)
dropdown.bind("<<ComboboxSelected>>", show_other)

other_entry = tk.Entry(card, width=30)

tk.Label(
    card,
    text = "Amount",
    bg = "white"
).pack()

amount_entry = tk.Entry(
    card,
    width = 30
)

amount_entry.pack(pady=8)

tk.Label(
    card,
    text = "Description",
    bg = "white"
).pack()

desc_entry = tk.Entry(card, width=30)
desc_entry.pack(pady=8)

tk.Button(
    card,text = "Save Expense",
    command = save_expense,
    bg='#3498db',
    fg = "white",
    width = 18,
    font = ("Times New Roman", 12, "bold")
).pack()

tk.Button(
    card,
    text="Open Dashboard",
    command=open_dashboard,
    bg="#2ecc71",
    fg="white",
    width=18,
    font=("Arial",11,"bold")
).pack(pady=10)


root.mainloop()