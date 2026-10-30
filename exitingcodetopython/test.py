
from abc import ABC, abstractmethod
import re


class AccountException(Exception):
    pass


class InvalidAmountException(AccountException):
    pass


class InvalidPinException(AccountException):
    pass


class InactiveAccountException(AccountException):
    pass


class AbstractAccount(ABC):

    def __init__(self, accountNumber, name, age, balance, accountType, status, pin):

        if age < 18:
            raise ValueError("Customer age must be 18 or above")

        if balance < 0:
            raise ValueError("Initial balance cannot be negative")

        if pin is None or not re.fullmatch(r"\d{4}", pin):
            raise ValueError("PIN must be 4 digits")

        self.accountNumber = accountNumber
        self.name = name
        self.age = age
        self.balance = balance
        self.accountType = accountType
        self.status = status
        self.pin = pin

    def validatePin(self, enteredPin):
        return self.pin is not None and self.pin == enteredPin

    def changePin(self, oldPin, newPin):
        if not self.validatePin(oldPin):
            return False

        if newPin is None or not re.fullmatch(r"\d{4}", newPin):
            return False

        self.pin = newPin
        return True

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountException("Deposit amount must be positive")

        self.balance += amount

    def withdraw(self, amount, enteredPin):
        if not self.validatePin(enteredPin):
            raise InvalidPinException("Invalid PIN entered")

        if self.status.upper() != "ACTIVE":
            raise InactiveAccountException("Account is not active")

        if amount <= 0:
            raise InvalidAmountException("Withdrawal amount must be positive")

        self.processDebit(amount)

    @abstractmethod
    def processDebit(self, amount):
        pass

    def displayAccountInfo(self):
        print("Account Number:", self.accountNumber)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Balance: Rs", self.balance)
        print("Account Type:", self.accountType)
        print("Status:", self.status)

    def getAccountNumber(self):
        return self.accountNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getBalance(self):
        return self.balance

    def getAccountType(self):
        return self.accountType

    def getStatus(self):
        return self.status
