# Import ABC and abstractmethod from the module abc (which stands for abstract base classes)
from abc import ABC, abstractmethod

# Class Bank


class Bank(ABC):
    def basicinfo(self):
        print("This is a generic bank")
        ret_statment = "Generic bank: 0"
        return ret_statment

    @abstractmethod
    def withdraw(self):
        pass

# Class Swiss


class Swiss(Bank):
    def __init__(self) -> None:
        super().__init__()
        self.bal = 1000

    def basicinfo(self):
        print("This is the Swiss Bank")
        ret_statement = f"Swiss Bank: {self.bal}"
        return ret_statement

    def withdraw(self, amount):
        if amount > self.bal:
            print("Insuffient funds")
        else:
            self.bal = self.bal - amount
            print(f"Withdrawn Amount: {amount}")
            print(f"New balance: {self.bal}")
        return super().withdraw()

# Driver Code


def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1000)


if __name__ == "__main__":
    main()
