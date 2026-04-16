# Smart Expense Tracker CLI Tool
# Created by Khushi

import json

# Load existing data (if any)
try:
    with open("expense_tracker.json", "r") as file:
        expense_data = json.load(file)
except FileNotFoundError:
    expense_data = {"salary": 0, "expenses": {}}

# Ask salary if not set
if expense_data["salary"] == 0:
    while True:
        try:
            salary = int(input("\nEnter Salary: "))
            if salary > 0:
                expense_data["salary"] = salary
                break
            else:
                print("Salary cannot be negative or 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number")

    with open("expense_tracker.json", "w") as file:
        json.dump(expense_data, file)

# Main Menu
while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Delete Expense\n4. Edit Expense\n5. Rename Category\n6. Exit")

    choice = input("\nEnter Your Choice: ")

    # ---------------- ADD EXPENSE ----------------
    if choice == "1":
        print("\nAdd Expense")
        print("-" * 30)

        while True:
            category = input("\nEnter Category (or type 'exit' to cancel): ")

            if category.lower() == "exit":
                print("Cancelled")
                break

            if not category.strip():
                print("Category cannot be empty")
            else:
                break

        if category.lower() == "exit":
            continue

        while True:
            amount_input = input("Enter Amount (or type 'exit' to cancel): ")

            if amount_input.lower() == "exit":
                print("Cancelled")
                break

            try:
                amount = int(amount_input)

                if amount >= 0:
                    expense_data["expenses"][category] = amount
                    with open("expense_tracker.json", "w") as file:
                        json.dump(expense_data, file)
                    print("\nExpense Added Successfully")
                    break
                else:
                    print("Amount cannot be negative")

            except ValueError:
                print("Invalid Input. Please enter a valid amount")

        if 'amount_input' in locals() and amount_input.lower() == "exit":
            continue

    # ---------------- VIEW EXPENSES ----------------
    elif choice == "2":
        if not expense_data["expenses"]:
            print("\nNo expenses found to view")
            continue

        print("\nExpense Summary")
        print("-" * 30)

        for category, amount in expense_data["expenses"].items():
            print(f"{category:<15}: {amount}")

        print("-" * 30)

        total_expenses = sum(expense_data["expenses"].values())
        remaining_salary = expense_data["salary"] - total_expenses

        print(f"\nTotal Expenses: {total_expenses}")
        print(f"Remaining Salary: {remaining_salary}")

        savings_percentage = (
            remaining_salary / expense_data["salary"] * 100
            if expense_data["salary"] > 0 else 0
        )

        print(f"Savings Percentage: {savings_percentage:.2f}%")

        if remaining_salary < 0:
            print("⚠️ You are overspending")
        elif savings_percentage > 50:
            print("Excellent saving habits")
        elif savings_percentage >= 30:
            print("Good, but can improve")
        else:
            print("Needs improvement")

    # ---------------- DELETE ----------------
    elif choice == "3":
        if not expense_data["expenses"]:
            print("\nNo expenses to delete")
            continue

        print("\nDelete Expense")
        print("-" * 30)

        print("Available Categories:")
        for category in expense_data["expenses"]:
            print("-", category)

        while True:
            delete_category = input("Enter category (or 'exit'): ")

            if delete_category.lower() == "exit":
                print("Cancelled")
                break

            if delete_category not in expense_data["expenses"]:
                print("Invalid category")
                continue
            break

        if delete_category.lower() == "exit":
            continue

        del expense_data["expenses"][delete_category]

        with open("expense_tracker.json", "w") as file:
            json.dump(expense_data, file)

        print("Expense deleted")

    # ---------------- EDIT ----------------
    elif choice == "4":
        if not expense_data["expenses"]:
            print("\nNo expenses to edit")
            continue

        print("\nEdit Expense")
        print("-" * 30)

        print("Available Categories:")
        for category in expense_data["expenses"]:
            print("-", category)

        while True:
            edit_category = input("Enter category (or 'exit'): ")

            if edit_category.lower() == "exit":
                print("Cancelled")
                break

            if edit_category not in expense_data["expenses"]:
                print("Invalid category")
                continue
            break

        if edit_category.lower() == "exit":
            continue

        while True:
            amount_input = input(f"Enter new amount (or 'exit'): ")

            if amount_input.lower() == "exit":
                print("Cancelled")
                break

            try:
                new_amount = int(amount_input)
                if new_amount >= 0:
                    expense_data["expenses"][edit_category] = new_amount
                    with open("expense_tracker.json", "w") as file:
                        json.dump(expense_data, file)
                    print("Updated successfully")
                    break
                else:
                    print("Amount cannot be negative")
            except ValueError:
                print("Invalid input")

        if amount_input.lower() == "exit":
            continue

    # ---------------- RENAME ----------------
    elif choice == "5":
        if not expense_data["expenses"]:
            print("\nNo categories to rename")
            continue

        print("\nRename Category")
        print("-" * 30)

        print("Available Categories:")
        for category in expense_data["expenses"]:
            print("-", category)

        while True:
            old_category = input("Enter category (or 'exit'): ")

            if old_category.lower() == "exit":
                print("Cancelled")
                break

            if old_category not in expense_data["expenses"]:
                print("Invalid category")
                continue
            break

        if old_category.lower() == "exit":
            continue

        while True:
            new_name = input("Enter new name (or 'exit'): ")

            if new_name.lower() == "exit":
                print("Cancelled")
                break

            if not new_name.strip():
                print("Cannot be empty")
                continue

            if new_name in expense_data["expenses"]:
                print("Already exists")
                continue
            break

        if new_name.lower() == "exit":
            continue

        expense_data["expenses"][new_name] = expense_data["expenses"].pop(old_category)

        with open("expense_tracker.json", "w") as file:
            json.dump(expense_data, file)

        print("Renamed successfully")

    # ---------------- EXIT ----------------
    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice")