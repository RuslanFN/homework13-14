class InsufficientFundsError(Exception):
    def __init__(self,balance,  *args: object) -> None:
        super().__init__('Недостаточно средств. Текущий баланс:' + str(balance), *args)

class BankAccaunt:
    """
    Класс имитации банковских операций
    Метод deposit(self, amount) - пополняет счёт на сумму amount
    >>> bank = BankAccaunt()
    >>> bank.deposit(100)
    >>> bank.get_balance()
    100

    Метод withdraw(self, amount) снимает деньги со счёта
    >>> bank = BankAccaunt()
    >>> bank.deposit(100)
    >>> bank.withdraw(50)
    >>> bank.get_balance()
    50
    >>> bank.withdraw(100)
    Traceback (most recent call last):
    ...
    InsufficientFundsError: Недостаточно средств. Текущий баланс:50
    >>> bank = BankAccaunt()
    >>> bank.get_balance()
    0
    >>> bank = BankAccaunt(100)
    Traceback (most recent call last):
    ...
    TypeError: BankAccaunt.__init__() takes 1 positional argument but 2 were given
    """
    def __init__(self) -> None:
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            raise InsufficientFundsError(self.balance)
    def get_balance(self):
        return self.balance

import doctest
doctest.testmod(verbose=True)