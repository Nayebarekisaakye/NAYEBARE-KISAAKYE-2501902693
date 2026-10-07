class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self._balance = float(initial_balance)

    @property
    def Balance(self) -> float:
        """Read-only current balance."""
        return self._balance

    def Deposit(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        self._balance += amount

    def Withdraw(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative.")
        if amount > self._balance:
            raise ValueError("Insufficient funds. Overdrafts are not allowed.")
        self._balance -= amount

    def __repr__(self) -> str:
        return f"BankAccount(Balance={self._balance:.2f})"
