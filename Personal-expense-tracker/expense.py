# -------------------------------------------------------------
# USER SETUP + BASIC VARIABLES
# -------------------------------------------------------------
import winsound





# Ask the user for their name
username = input("Provide your name: ")

# Convert the name to title case (e.g., "ameenur" → "Ameenur")
username_1 = username.title()

# Ask the user for their starting balance (float allows decimals)
balance = float(input("Please provide your starting amount: "))

# List to store every expense the user enters
expenses = []

# Dictionary to store total spent per category (e.g., food, travel)
spending_habits = {}

# Simple tracker flag
tracking_live = True

# Exit message for the menu
exit_m = "Thanks for using our service, have a nice day!"

# ---------------- TERMINAL COLOUR CODES ----------------
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
RESET = "\033[0m"


# -------------------------------------------------------------
# FUNCTION: Show welcome message
# -------------------------------------------------------------
def show_welcome():
    print(CYAN + "----------------------------------------" + RESET)
    print(GREEN + f"Welcome, {username_1}!" + RESET)
    print(YELLOW + f"Current balance: £{balance}" + RESET)
    print(BLUE + f"Tracker status: {tracking_live}" + RESET)
    print(CYAN + "----------------------------------------" + RESET)


# -------------------------------------------------------------
# FUNCTION: Add an expense
# -------------------------------------------------------------
def add_expense(amount, category):
    global balance

    expenses.append(amount)
    balance -= amount
    update_spending_habits(category, amount)

    print(GREEN + f"Expense of £{amount} added under '{category}'!" + RESET)
    print(YELLOW + f"New balance: £{balance}" + RESET)

    return balance


# -------------------------------------------------------------
# FUNCTION: Calculate total expenses
# -------------------------------------------------------------
def calculate_total_expenses():
    total = sum(expenses)

    print(CYAN + f"Total spent so far: £{total}" + RESET)
    return total


# -------------------------------------------------------------
# FUNCTION: Update spending habits dictionary
# -------------------------------------------------------------
def update_spending_habits(category, amount):
    if category in spending_habits:
        spending_habits[category] += amount
    else:
        spending_habits[category] = amount

    print(BLUE + f"Updated category '{category}': £{spending_habits[category]}" + RESET)
    return spending_habits


# -------------------------------------------------------------
# EXPENSE TRACKER MENU SYSTEM
# -------------------------------------------------------------

show_welcome()

while True:
    print(CYAN + "\n--- Expense Tracker Menu ---" + RESET)
    print(YELLOW + "1. Add expense" + RESET)
    print(YELLOW + "2. Show total spent" + RESET)
    print(YELLOW + "3. Show spending habits" + RESET)
    print(YELLOW + "4. Show balance" + RESET)
    print(RED + "5. Exit" + RESET)

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter expense amount: "))
        category = input("Enter category: ")
        add_expense(amount, category)

        # SUCCESS SOUND
        winsound.Beep(700, 200)

    elif choice == "2":
        calculate_total_expenses()
        winsound.Beep(600, 150)

    elif choice == "3":
        print(BLUE + f"Spending habits: {spending_habits}" + RESET)
        winsound.Beep(600, 150)

    elif choice == "4":
        print(YELLOW + f"Current balance: £{balance}" + RESET)
        winsound.Beep(600, 150)

    elif choice == "5":
        print(GREEN + exit_m + RESET)

        # EXIT SOUND (lower pitch)
        winsound.Beep(400, 300)
        break

    else:
        print(RED + "Invalid choice, try again." + RESET)

        # ERROR SOUND
        winsound.Beep(200, 300)

