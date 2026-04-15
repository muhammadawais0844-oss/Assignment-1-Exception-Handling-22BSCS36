import sys

# --- 1. Custom Exception ---
class InsufficientFundsError(Exception):
    """Raised when a user tries to withdraw more than their balance."""
    pass

class ATMSystem:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self):
        try:
            # --- 2. Input Validation (ValueError Handling) ---
            amount = float(input("Enter amount to withdraw: "))
            
            if amount <= 0:
                print("Error: Amount must be positive.")
                return

            if amount > self.balance:
                # --- 3. Raising Custom Exception ---
                raise InsufficientFundsError(f"Overdraft! You only have ${self.balance}")

            self.balance -= amount
            print(f"Withdrawal successful! New balance: ${self.balance}")

        except ValueError:
            print("Invalid Input: Please enter a numeric value (e.g., 500).")
        except InsufficientFundsError as e:
            print(f"Transaction Failed: {e}")
        except Exception as e:
            # Catch-all for unexpected runtime errors to prevent crash
            print(f"An unexpected system error occurred: {e}")

    def show_balance(self):
        print(f"Current Balance: ${self.balance}")

def main():
    atm = ATMSystem(1000) # Initial deposit
    
    while True:
        print("\n--- Mini ATM Menu ---")
        print("1. Check Balance\n2. Withdraw\n3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            atm.show_balance()
        elif choice == '2':
            atm.withdraw()
        elif choice == '3':
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()