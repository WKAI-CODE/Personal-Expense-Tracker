# Personal Expense Tracker
# This program records expenses and calculates spending summaries.
import csv
     
def display_menu():
    print("\n" + "=" * 40)
    print("     Personal Expense Tracker Menu")
    print("=" * 40)
    print(" 1. Add Expense")
    print(" 2. View All Expenses")
    print(" 3. View Total Spending")
    print(" 4. View Spending By Category")
    print(" 5. Search Expenses By Category")
    print(" 0. Exit")
    print("=" * 40)


def add_expense():
    print("\n" + "=" * 40)
    print("             Add Expense")
    print("=" * 40)

    date = input("Enter date: ").strip()
    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    if not date or not category or not description:
        print("All fields must be completed.")
        return

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return
    
    if amount <= 0:
        print("Invalid amount. Amount must be greater than zero.")
        return
    
    # encoding="utf-8" means supports many characters and languages
    with open ("expenses.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

        print("\nExpense added successfully.")
    
    return


def view_expenses():
    print("\n" + "=" * 65)
    print("                     View All Expenses")
    print("=" * 65)

    try:
        with open("expenses.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            # Skip the CSV heading row rows
            next(reader, None)

            print(
                # < means align to the left, > is right and ^ is centre, 15 is the amount of space
                f"{'Date':<15}"         
                f"{'Category':<16}"
                f"{'Description':<21}"
                f"{'Amount':>10}"
            )
            print("-" * 65)    

            expense_found = False                 

            for row in reader:
                if len(row) != 4:
                    continue

                date = row[0]
                category = row[1]
                description = row[2]
                amount = float(row[3])

                expense_found = True

                print(
                    f"{date:<15}"
                    f"{category:<16}"
                    f"{description:<22}"
                    f"RM{amount:>7.2f}"
                )

            if not expense_found:
                print("No expense records found.")
                return

    except FileNotFoundError:
        print("Expense file was not found.")

    except ValueError:
        print("An expense contains an invalid amount.")
    

def view_total_spending():
    print("\n" + "=" * 40)
    print("          View Total Spending")
    print("=" * 40)

    total = 0.0
    expense_count = 0

    try:
        with open ("expenses.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            next(reader, None)

            for row in reader:
                if len(row) != 4:
                    continue

                amount = float(row[3])
                total += amount
                expense_count += 1

        print(f"Number of Expenses: {expense_count}")
        print(f"Total Spending = RM {total:.2f}")

    except FileNotFoundError:
        print("Expense file was not found.")

    except ValueError:
        print("An expense contains an invalid amount.")


def view_spending_by_category():
    print("\n" + "=" * 40)
    print("           Spending By Category")
    print("=" * 40)

    category_totals = {}

    try:
        with open ("expenses.csv", "r", encoding= "utf-8") as file:
            reader = csv.reader(file)

            next(reader, None)

            for row in reader:
                if len(row) != 4:
                    continue

                category = row[1].strip().title()
                amount = float(row[3])

                if category in category_totals:
                    category_totals[category] += amount
                else:
                    category_totals[category] = amount

            if not category_totals:
                print("No expenses records found.")
                return
            else:
                print(f"{'Category':<25}{'Total':>13}")
                print("-" * 40)

                for category, total in category_totals.items():
                    print(f"{category:<28}RM{total:>8.2f}")

                print("-" * 40)

    except FileNotFoundError:
        print("Expense file was not found.")

    except ValueError:
        print("An expense contains an invalid amount.")


def search_expenses_by_category():
    print("\n" + "=" * 65)
    print("                   Search Expenses By Category")
    print("=" * 65)

    search = input("Enter category to search: ").strip().title()

    if not search: 
        print("Category cannot be empty.")
        return
    
    record_found = 0
    category_total = 0.0
    
    try:
        with open ("expenses.csv", "r", encoding= "utf-8") as file:
            reader = csv.reader(file)

            next(reader, None)
            
            print( "\n" + "-" * 65)
            print(
                f"{'Date':<15}"         
                f"{'Category':<16}"
                f"{'Description':<21}"
                f"{'Amount':>10}"
            )
            print("-" * 65)

            category_found = False

            for row in reader:
                if len(row) != 4:
                    continue
            
                date = row[0]
                category = row[1].strip().title()
                description = row[2]
                amount = float(row[3])
                
                
                if category == search:
                    category_found = True
                    record_found += 1
                    category_total += amount
                    print(
                        f"{date:<15}"
                        f"{category:<16}"
                        f"{description:<22}"
                        f"RM{amount:>7.2f}"
                    )

            if not category_found:
                print("No expenses found for this category.")
            else:
                print(f"\nRecord Found: {record_found}")
                print(f"Category Total: RM {category_total:.2f}")

    except FileNotFoundError:
        print("Expense file was not found.")

    except ValueError:
        print("An expense contains an invalid amount.")


def main():
    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()
        
        elif choice == "2":
            view_expenses()

        elif choice == "3":
            view_total_spending()

        elif choice == "4":
            view_spending_by_category()

        elif choice == "5":
            search_expenses_by_category()

        elif choice == "0":
            print("Thank you for using the program.")
            break

        else:
            print("Invalid choice! Please enter a number from 0 to 5.")

if __name__ == "__main__":
    main()