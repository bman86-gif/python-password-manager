








print("Brandon's Personal Password Manager")
print("1. CLI Mode")
print("2. GUI Mode")
choice = input("Choose Your Desired Interface ")
if choice == "1":
    from cli import run_cli
    run_cli()
elif choice == "2":
    from gui import run_gui
    run_gui()
