class BankAccount:
    all_accounts = []

    def __init__(self, account_holder, account_number, balance=0.0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        BankAccount.all_accounts.append(self)
        
    @property
    def account_holder(self):
        return self.__account_holder
    @account_holder.setter
    def account_holder(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Account holder name must be a string and not empty.")
        self.__account_holder = value
    @property
    def account_number(self):
        return self.__account_number
    @account_number.setter
    def account_number(self,value):
        if not isinstance(value, str) or not value.isdigit() or len(value) != 10:
            raise ValueError("Account number must be 10 digits.")
        self.__account_number = value
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,value):
        if value<0:
            raise ValueError("Balance cannot be negative.")
        self.__balance=value
        
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount

    def withdraw(self, amount):
        if amount<=0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient balance.")
        self.__balance -= amount

    def display_details(self):
        print(f"Account Holder: {self.__account_holder}")
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: {self.__balance}")

    def __repr__(self):
        return f"BankAccount('{self.__account_holder}', '{self.__account_number}', {self.__balance})"

if __name__ == "__main__":
    account1 = BankAccount("Vignesh", "1234567890", 5000)
    account2 = BankAccount("Arun", "9876543210")

    account1.deposit(2000)
    account1.withdraw(1000)

    account1.display_details()
    print(BankAccount.all_accounts)