"""
password.py is for password entry storage
"""

from datetime import datetime


class Password:
    """
    Represents a single password entry in the password manager.

    Attributes:
        account (str): The account name/label (e.g., "Gmail", "Twitter")
        username (str): The username for this account
        password (str): The actual password
        created_date (str): When this entry was created
    """

    def __init__(self, account, username, password):
        """
        Initialize a new password entry.

        Args:
            account (str): Account name/label (e.g., "Gmail")
            username (str): Username for the account
            password (str): The password
        """
        self.account = account
        self.username = username
        self.password = password
        self.created_date = datetime.now().strftime("%Y-%m-%d")

    def __str__(self):
        """
        Return a readable string representation of this password entry.
        """
        return f"Account: {self.account}\nUsername: {self.username}\nPassword: {'*' * len(self.password)}\nCreated: {self.created_date}"  # "*******" instead of actual password plain text

    def to_dict(self):
        """
        Convert this password object to a dictionary for saving to JSON.
        """
        return {
            "account": self.account,
            "username": self.username,
            "password": self.password,
            "created_date": self.created_date
        }

    @staticmethod
    def from_dict(data):
        """
        Create a Password object from a dictionary (when loading from JSON).
        """
        pwd = Password(data["account"], data["username"], data["password"])
        pwd.created_date = data["created_date"]  # the created_date that it's talking about lol

        return pwd
