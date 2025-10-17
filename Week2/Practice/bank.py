class BankAccount:
    """
    A simple BankAccount class to perform basic banking operations.
    """

    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional initial balance."""
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the bank account."""
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited: {amount}")
        else:
            print("⚠ Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money; show message if insufficient balance."""
        if amount <= 0:
            print("⚠ Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("❌ Insufficient balance!")
        else:
            self.balance -= amount
            print(f"💰 Withdrawn: {amount}")

    def check_balance(self):
        """Display the current balance of the account."""
        print(f"💳 Current Balance: {self.balance}")


# ------------------- Interactive Banking App -------------------
print("🏦 Welcome to Python Bank 🏦")
account = BankAccount(int(input("Enter initial balance: ")))

while True:
    print("\nChoose an option:")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amount = int(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == "2":
        amount = int(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        print("👋 Thank you for banking with us!")
        break

    else:
        print("⚠ Invalid choice! Please select 1-4.")
