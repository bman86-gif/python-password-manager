# Password Manager

A personal password manager built from scratch in Python as a learning project. Features both CLI and GUI interfaces (GUI in development) with plans for encryption.

## Project Status

**Current:** CLI interface functional with visual enhancements in progress
**Next:** Complete CLI polish, then GUI implementation
**Future:** Add encryption to secure stored passwords

## Features

### Implemented
- Add passwords manually
- Generate secure passwords with customizable options (length, uppercase, special chars, digits)
- View stored passwords
- List all accounts
- Update existing passwords (requires old password verification)
- Delete passwords
- Persistent storage (JSON file)

### In Progress
- ANSI color-coded output (errors in red, success in green, etc.)
- Box-drawing for menu display
- Formatted tables for password listing

### Planned
- GUI interface using tkinter
- Password encryption using `cryptography` library
- Master password protection
- Copy to clipboard functionality
- Password strength indicator
- Search/filter accounts
- Backup/export feature

## Project Structure

```
PyCharmMiscProject/
├── main.py                 # Entry point - choose CLI or GUI
├── password.py             # Password class (data model)
├── password_manager.py     # PasswordManager class (CRUD operations)
├── generate_passwords.py   # Password generation with user options
├── cli.py                  # Command-line interface
├── cli_colors.py           # ANSI colors and formatting utilities
├── gui.py                  # GUI interface (in development)
├── passwords.json          # Data storage (auto-created)
├── CLI_ENHANCEMENT_PLAN.md # Implementation plan for CLI visuals
└── README.md               # This file
```

## How to Run

```bash
# Run the main application
python main.py

# Or run CLI directly
python cli.py
```

### CLI Menu Options

1. **Add new password (manual)** - Enter account, username, password yourself
2. **Generate new password** - Enter account/username, password is generated
3. **View password** - Look up a specific account
4. **List all accounts** - See all stored accounts in a table
5. **Update password** - Change password (requires old password)
6. **Delete password** - Remove an account
7. **Quit** - Exit the program

## Architecture

The project follows separation of concerns:

**Core Layer (Backend)**
- `Password` class - represents a single password entry
- `PasswordManager` class - handles all CRUD operations and file I/O
- `generate_password()` - utility function for secure password generation

**Interface Layer (Frontend)**
- `cli.py` - command-line interface that uses the core layer
- `gui.py` - graphical interface that will use the same core layer

Both interfaces share the same backend, so features only need to be implemented once.

## What I Learned Building This

### Python Fundamentals
- Classes and OOP (Password, PasswordManager, Colors, BoxChars)
- File I/O with JSON serialization
- List comprehensions
- String formatting with f-strings
- Error handling with try/except

### CLI Development
- Input validation with while loops
- ANSI escape codes for terminal colors
- Unicode box-drawing characters
- Building reusable utility functions

### Software Design
- Separation of concerns (backend vs interface)
- DRY principle (Don't Repeat Yourself)
- Making code modular and reusable

## Roadmap

### Phase 1: CLI Enhancement (Current)
- [x] Basic CLI functionality
- [x] Input validation
- [ ] Color-coded output
- [ ] Box-drawing for menus
- [ ] Table formatting for lists

### Phase 2: GUI Development
- [ ] Basic tkinter window
- [ ] Entry fields for account/username/password
- [ ] Buttons for CRUD operations
- [ ] Listbox showing all accounts
- [ ] Generate password button

### Phase 3: Security
- [ ] Encrypt passwords before saving
- [ ] Master password to unlock the app
- [ ] Secure password handling in memory

### Phase 4: Polish
- [ ] Copy to clipboard
- [ ] Password strength meter
- [ ] Search functionality
- [ ] Import/export passwords
- [ ] Better error messages

## Dependencies

Currently uses Python standard library only:
- `json` - data serialization
- `datetime` - timestamps
- `random` - password generation
- `string` - character sets for passwords
- `tkinter` - GUI (planned, built into Python)

Future:
- `cryptography` - for password encryption

## Notes

This is a learning project. The goal is to understand Python deeply by building something real, not just copying tutorials. Every line was written by hand with guidance when stuck.

Passwords are currently stored in plain text in `passwords.json`. **Do not use this for real passwords until encryption is implemented.**

## License

Personal project - do whatever you want with it.
