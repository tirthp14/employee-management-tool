import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import json
import csv
from statistics import mean
from PIL import Image, ImageTk

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

# Export data to CSV
def export_to_csv():
    with open("employee_data.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Designation", "Department", "Salary"])
        for emp_id, details in Emp_Data.items():
            writer.writerow([emp_id, details['Employee Name'], details['Employee Designation'],
                             details['Employee Department'], details['Employee Salary']])
    messagebox.showinfo("Success", "Data exported to employee_data.csv")

# Add employee photo upload functionality
def upload_photo():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        photo = Image.open(file_path)
        photo.thumbnail((80, 80))
        photo = ImageTk.PhotoImage(photo)
        photo_label.config(image=photo)
        photo_label.image = photo

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
        display_employees()  # Refresh list
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter the correct data.")

# Function to display employee details
def display_employees():
    emp_list.delete(*emp_list.get_children())  # Clear the treeview first
    if not Emp_Data:
        messagebox.showinfo("Info", "No employee details found.")
    else:
        for emp_id, details in Emp_Data.items():
            emp_list.insert("", "end", values=(
                emp_id, details['Employee Name'], details['Employee Designation'],
                details['Employee Department'], details['Employee Salary']))

# Function to search employees
def search_employee():
    emp_list.delete(*emp_list.get_children())  # Clear the list first
    query = search_entry.get().lower()
    if not query:
        display_employees()
        return

    for emp_id, details in Emp_Data.items():
        if (query in details['Employee Name'].lower() or 
            query in details['Employee Department'].lower()):
            emp_list.insert("", "end", values=(
                emp_id, details['Employee Name'], details['Employee Designation'],
                details['Employee Department'], details['Employee Salary']))

# Function to delete employee
def delete_employee():
    selected_item = emp_list.selection()
    if selected_item:
        emp_id = emp_list.item(selected_item)['values'][0]
        del Emp_Data[emp_id]
        save_data()
        emp_list.delete(selected_item)
        messagebox.showinfo("Success", "Employee deleted successfully!")
    else:
        messagebox.showerror("Error", "Please select an employee to delete.")

# Function to update employee details
def update_employee():
    selected_item = emp_list.selection()
    if selected_item:
        emp_id = emp_list.item(selected_item)['values'][0]
        entry_id.insert(0, emp_id)
        entry_name.insert(0, Emp_Data[emp_id]['Employee Name'])
        entry_designation.insert(0, Emp_Data[emp_id]['Employee Designation'])
        entry_department.insert(0, Emp_Data[emp_id]['Employee Department'])
        entry_salary.insert(0, Emp_Data[emp_id]['Employee Salary'])

        # Remove the old entry for update
        delete_employee()

# Function to sort employees
def sort_employees_by(field):
    sorted_data = sorted(Emp_Data.items(), key=lambda x: x[1][field])
    emp_list.delete(*emp_list.get_children())  # Clear the treeview
    for emp_id, details in sorted_data:
        emp_list.insert("", "end", values=(
            emp_id, details['Employee Name'], details['Employee Designation'],
            details['Employee Department'], details['Employee Salary']))

# Function to clear input fields
def clear_entries():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_designation.delete(0, tk.END)
    entry_department.delete(0, tk.END)
    entry_salary.delete(0, tk.END)

# Employee Analytics
def show_analytics():
    total_employees = len(Emp_Data)
    total_salary = sum(details['Employee Salary'] for details in Emp_Data.values())
    avg_salary = mean([details['Employee Salary'] for details in Emp_Data.values()]) if Emp_Data else 0
    messagebox.showinfo("Analytics", f"Total Employees: {total_employees}\nTotal Salary: ${total_salary:.2f}\nAverage Salary: ${avg_salary:.2f}")

# Tkinter Window setup
root = tk.Tk()
root.title("TeamTracker - Employee Management")
root.geometry("900x600")
root.config(bg='#f0f0f0')

# Labels and Entry Widgets for Input
label_id = tk.Label(root, text="Employee ID", bg='#f0f0f0')
label_id.grid(row=0, column=0)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1)

label_name = tk.Label(root, text="Employee Name", bg='#f0f0f0')
label_name.grid(row=1, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1)

label_designation = tk.Label(root, text="Designation", bg='#f0f0f0')
label_designation.grid(row=2, column=0)
entry_designation = tk.Entry(root)
entry_designation.grid(row=2, column=1)

label_department = tk.Label(root, text="Department", bg='#f0f0f0')
label_department.grid(row=3, column=0)
entry_department = tk.Entry(root)
entry_department.grid(row=3, column=1)

label_salary = tk.Label(root, text="Salary", bg='#f0f0f0')
label_salary.grid(row=4, column=0)
entry_salary = tk.Entry(root)
entry_salary.grid(row=4, column=1)

# Buttons for CRUD operations
btn_add = tk.Button(root, text="Add Employee", command=add_employee)
btn_add.grid(row=5, column=0)

btn_update = tk.Button(root, text="Update Employee", command=update_employee)
btn_update.grid(row=5, column=1)

btn_delete = tk.Button(root, text="Delete Employee", command=delete_employee)
btn_delete.grid(row=5, column=2)

# Search functionality
search_label = tk.Label(root, text="Search by Name/Dept", bg='#f0f0f0')
search_label.grid(row=0, column=2)
search_entry = tk.Entry(root)
search_entry.grid(row=0, column=3)
btn_search = tk.Button(root, text="Search", command=search_employee)
btn_search.grid(row=0, column=4)

# Treeview (Table) to display employees
columns = ("ID", "Name", "Designation", "Department", "Salary")
emp_list = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    emp_list.heading(col, text=col)
emp_list.grid(row=6, column=0, columnspan=5)

# Sorting Options
sort_label = tk.Label(root, text="Sort by", bg='#f0f0f0')
sort_label.grid(row=7, column=0)
sort_name = tk.Button(root, text="Name", command=lambda: sort_employees_by("Employee Name"))
sort_name.grid(row=7, column=1)
sort_salary = tk.Button(root, text="Salary", command=lambda: sort_employees_by("Employee Salary"))
sort_salary.grid(row=7, column=2)

# Analytics Button
btn_analytics = tk.Button(root, text="Show Analytics", command=show_analytics)
btn_analytics.grid(row=7, column=3)

# Export to CSV Button
btn_export = tk.Button(root, text="Export to CSV", command=export_to_csv)
btn_export.grid(row=7, column=4)

# Photo upload feature
photo_label = tk.Label(root, text="Upload Employee Photo", bg='#f0f0f0')
photo_label.grid(row=8, column=0)
btn_upload_photo = tk.Button(root, text="Upload Photo", command=upload_photo)
btn_upload_photo.grid(row=8, column=1)

# Load data from file on startup
load_data()
display_employees()

root.mainloop()
