class Account:
    def __init__(self, name):
        """
        Creates new account class instance
        """
        self.account_name = name
        self.account_balance = 0

    def deposit(self, amount):
        """"
        Deposits given amount into account
        :param amount: The amount given to deposit
        :return: True of the deposit was successful, False otherwise.
        """
        if amount > 0:
            self.account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        """
        Takes out amount of money given from the account
        :param amount: The amount of money to withdraw.
        :return: True if the withdrawal was successful, False otherwise.
        """
        if (amount > 0) and (amount <= self.account_balance):
            self.account_balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        """
        Returns current balance
        :return: The current balance of the account.
        """
        return self.account_balance

    def get_name(self):
        """
        Returns name of the account owner
        :return: The name of the account owner.
        """
        return self.account_name