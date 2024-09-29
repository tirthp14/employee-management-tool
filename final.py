import tkinter as tk
from tkinter import messagebox
import json

# Data storage for employees
Emp_Data = {}

# Load data from JSON file
def load_data():
    global Emp_Data
    try:
        with open("employee_data.json", "r") as f:
            Emp_Data = json.load(f)
    except FileNotFoundError:
        Emp_Data = {}

# Save data to JSON file
def save_data():
    with open("employee_data.json", "w") as f:
        json.dump(Emp_Data, f)

# Function to add employee data
def add_employee():
    try:
        emp_id = int(entry_id.get())
        if emp_id in Emp_Data:
            messagebox.showerror("Error", "Employee ID already exists!")
            return
        emp_name = entry_name.get()
        emp_designation = entry_designation.get()
        emp_department = entry_department.get()
        emp_salary = float(entry_salary.get())

        Emp_Data[emp_id] = {
            "Employee Name": emp_name,
            "Employee Designation": emp_designation,
            "Employee Department": emp_department,
            "Employee Salary": emp_salary
        }
        save_data()
        messagebox.showinfo("Success", "Employee added successfully!")
        clear_entries()
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter the correct data.")

# Function to display employee details
def display_employees():
    emp_list.delete(0, tk.END)  # Clear the listbox first
    if not Emp_Data:
        emp_list.insert(tk.END, "No employee details found.")
    else:
        for emp_id, details in Emp_Data.items():
            emp_list.insert(tk.END, f"ID: {emp_id}, Name: {details['Employee Name']}")

# Function to clear input fields
def clear_entries():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_designation.delete(0, tk.END)
    entry_department.delete(0, tk.END)
    entry_salary.delete(0, tk.END)

# Tkinter Window setup
root = tk.Tk()
root.title("TeamTracker - Employee Management")
root.geometry("500x400")

# Labels and Entry Widgets for Input
label_id = tk.Label(root, text="Employee ID")
label_id.grid(row=0, column=0)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1)

label_name = tk.Label(root, text="Employee Name")
label_name.grid(row=1, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1)

label_designation = tk.Label(root, text="Designation")
label_designation.grid(row=2, column=0)
entry_designation = tk.Entry(root)
entry_designation.grid(row=2, column=1)

label_department = tk.Label(root, text="Department")
label_department.grid(row=3, column=0)
entry_department = tk.Entry(root)
entry_department.grid(row=3, column=1)

label_salary = tk.Label(root, text="Salary")
label_salary.grid(row=4, column=0)
entry_salary = tk.Entry(root)
entry_salary.grid(row=4, column=1)

# Buttons to Add and Display Employees
btn_add = tk.Button(root, text="Add Employee", command=add_employee)
btn_add.grid(row=5, column=0)

btn_display = tk.Button(root, text="Display Employees", command=display_employees)
btn_display.grid(row=5, column=1)

# Listbox to display employees
emp_list = tk.Listbox(root, width=50)
emp_list.grid(row=6, column=0, columnspan=2)

# Load data on startup
load_data()

root.mainloop()
