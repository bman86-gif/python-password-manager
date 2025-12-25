from password_manager import PasswordManager
from generate_passwords import generate_password
from cli_colors import error, success, warning, info, draw_box, draw_table
def display_menu():
    print("\n=== Password Manager ===")
    print("1. Add new password (manual)")
    print("2. Generate new password")
    print("3. View password")
    print("4. List all accounts")
    print("5. Update Password")
    print("6. Delete Password")
    print("7. Quit already")

    print("=======================\n")

def run_cli():
    manager = PasswordManager()
    while True:
        display_menu()
        choice = input("Enter choice (1-7): ").strip()
        if not choice or choice < "1" or choice > "7":
            print("[ERROR] Invalid selection, you wanker! Try again mate (1-7)")
            continue


#=====================================================================================================

        if choice == "1":

           while True:
                account = input("Enter account name (e.g., Gmail): ").strip()
                if not account:
                    print("[ERROR] Can't be empty, Bonehead!")
                    continue
                break
           while True:
                username = input("Enter username/email: ").strip()
                if not username:
                    print("[ERROR] Can't be empty, Bonehead!")
                    continue
                break
           while True:
                password = input("Enter password: ").strip()
                if not password:
                    print("[ERROR] Can't be empty, Bonehead!")
                    continue
                break
           if manager.add_password(account, username, password):
                print("[INFO] Password added!")
                manager.save_to_file()
           else:
                print("[ERROR] Account already exists!")
#===============================================================================================
        elif choice == "2":

            while True:
                account = input("Enter account name (e.g., Gmail): ").strip()
                if not account:
                    print("[ERROR] Can't be empty, Bonehead!")
                    continue
                break
            while True:
                username = input("Enter username/email: ").strip()
                if not username:
                    print("[ERROR] Can't be empty, Bonehead!")
                    continue
                break
            print("[INFO] Let's generate a password...")
            password = generate_password()

            if manager.add_password(account, username, password):
                print("[SUCCESS] Password Generated and saved!")
                print("f[INFO] Your password: {password}")
                manager.save_to_file()
            else:
                print("[ERROR] Account already exists!")
#================NUMBER3==============================================================================
        elif choice == "3":
            while True:
                account = input("Enter the account you want to view: ").strip()
                if not account:
                    print("Really Bro? Try again you wanker!")
                    continue
                break
            pwd_obj = manager.get_password(account)
            if pwd_obj:
                print(f"account: {pwd_obj.account}")
                print(f"Username: {pwd_obj.username}")
                print(f"Password: {pwd_obj.password}")
            else:
                print("[ERROR] Account not found! 😔")
#===================NUMBER4===========================================================================
        elif choice == "4":
            if len(manager.passwords) == 0:
                print("No passwords saved yet!")
            else:
                print("\n=== All Accounts ===")
                for pwd in manager.passwords:
                    print(f"- {pwd.account} ({pwd.username})")
                print("===========================\n")


#=============NUMBER5=================================================================================
        elif choice == "5":
            while True:
                account = input("Enter account name/email to update ").strip()
                if not account:
                    print("Really Bro? Try again you wanker!")
                    continue
                break
            while True:
                old_password = input("Enter the old password for this account ")
                if not old_password:
                    print("Really Bro? Try again you wanker!")
                    continue
                break
            while True:
                new_password = input("Enter the new password ")
                if not new_password:
                    print("Really Bro? Try again you wanker!")
                    continue
                break


            if manager.update_password_securely(account, old_password, new_password):
                manager.save_to_file()
                print("[INFO] Password updated!")
            else:
                print("[ERROR] Wrong password, or account not found, You have to want it!")

#=====================================================================================================
        elif choice == "6":
            while True:
                dead_account_walking = input("Enter the account you want to 86 ").strip()
                if not dead_account_walking:
                    print("Really Bro? Enter SOMETHING at least!")
                    continue
                break
            manager.delete_password(dead_account_walking)



        elif choice == "7":
            exit()
#=====================================================================================================












