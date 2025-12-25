
# password_manager.py
import json
from password import Password


class PasswordManager:
    def __init__(self, file_path="passwords.json"):
        self.file_path = file_path
        self.passwords = []
        self.load_from_file()

    def load_from_file(self):
        try:
            # We try to open the file for reading ('r' = read mode)
            with open(self.file_path, 'r') as file:
                # Read the file and parse it as JSON
                data = json.load(file) # data is now a list of dictionaries
                # Convert each dictionary back to a Password object
                # Remember: Password.from_dict() converts a dict to a Password object
                self.passwords = [Password.from_dict(pwd) for pwd in data]
        except FileNotFoundError:
            self.passwords = []
    def save_to_file(self):
        """
        save all passwords to the JSON file.
        We call this after any add/update/delete operation.
                """
        with open(self.file_path, 'w') as file:
            # Convert all Password objects back to dictionaries
            # Remember: pwd.to_dict() converts a Password object to a dictionary
            data = [pwd.to_dict() for pwd in self.passwords]
            # write the list of dictionaries to the file as JSON
            # indent=2 makes it pretty and readable
            json.dump (data, file, indent=2)


    def add_password(self, account, username, password):
        """
        Add a new password entry
        Args:
             account (str): Account name (someone, "Gmail")
             username: (str): Username (e.g., "John@gmail.com")
             password: (str): Password (e.g., "swordsmanship123")
        Returns:
            bool: True if added successfully, False if account already exists



        Check if this account ALREADY exists
        This checks if ANY password object has this account name
        .lower() makes the comparison case-insensitive (Gmail = gmail)
        """
        if any(pwd.account.lower() == account.lower() for pwd in self.passwords):
            return False # Account already exists so don't add it!

        # If we get here, the account doesn't exist, so create a new Password object
        new_password = Password(account, username, password)
        self.passwords.append(new_password)
        return True

    def update_password_securely(self, account, old_password, new_password):
        for pwd in self.passwords:
            if pwd.account.lower() == account.lower():
                if pwd.password ==  old_password:
                    pwd.password = new_password
                    return True
                else:
                    return False
        return False


    def get_password(self, account):
        """
        Find and return a password by account name.

        Args:
            account (str): The account name to search for (e.g., "Gmail")

        Returns:
            Password: The Password object if found, None if not found
            :param account:
            :param self:
        """
        # Loop through all passwords
        for pwd in self.passwords:
            # Check if this password's account matches (case-insensitive)
            if pwd.account.lower() == account.lower():
                # Found it! Return this Password object
                return pwd
        return None

    def delete_password(self, dead_account_walking):
        """
        Delete a password entry by account name.

        Args:
            account (str): The account name to delete

        Returns:
            bool: True if deleted, False if account not found
            :param self:
            :param dead_account_walking: # 😄😄😄
        """
        # Loop through all passwords
        for pwd in self.passwords:
            # Check if this password's account matches
            if pwd.account.lower() == dead_account_walking.lower():
                # Found it! Remove it from the list
                self.passwords.remove(pwd)
                # Save the updated list to file
                self.save_to_file()
                # Return True to show it worked
                return True

        return False

