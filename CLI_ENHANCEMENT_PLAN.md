# Password Manager CLI - Enhancement Plan

## Overview

This plan covers everything needed to transform your basic CLI into a professional-looking terminal application with colors, boxes, tables, and bug fixes.

**Files you'll create:**
- `cli_colors.py` - Reusable color and formatting utilities

**Files you'll modify:**
- `cli.py` - Apply visual enhancements and fix bugs

**Files unchanged:**
- `password_manager.py`, `password.py`, `generate_passwords.py`, `main.py`

---

## Phase 1: Color Utilities

**File:** `cli_colors.py` (create new)

**Goal:** Build ANSI color codes from scratch (no libraries)

### Understanding ANSI Escape Codes

```
Structure: \033[<code>m
- \033[ = escape sequence start
- <code> = the color/style code
- m = end of sequence
- \033[0m = reset to default
```

### Code to Write

```python
# cli_colors.py

class Colors:
    """ANSI color codes for terminal output."""

    # Text colors (bright versions: 90-97)
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'

    # Styles
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # Reset
    RESET = '\033[0m'


def colorize(text, color):
    """Wrap text with color code and reset."""
    return f"{color}{text}{Colors.RESET}"


def error(text):
    """Red text for errors."""
    return colorize(text, Colors.RED)


def success(text):
    """Green text for success messages."""
    return colorize(text, Colors.GREEN)


def warning(text):
    """Yellow text for warnings."""
    return colorize(text, Colors.YELLOW)


def info(text):
    """Blue text for informational messages."""
    return colorize(text, Colors.BLUE)


def heading(text):
    """Cyan bold text for headings."""
    return colorize(text, Colors.CYAN + Colors.BOLD)
```

### Test Code (add at bottom)

```python
if __name__ == "__main__":
    print(error("[ERROR] This is red"))
    print(success("[SUCCESS] This is green"))
    print(warning("[WARNING] This is yellow"))
    print(info("[INFO] This is blue"))
    print(heading("=== HEADING ==="))
```

### Verify

```bash
python cli_colors.py
```

You should see colored output. If not, your terminal may not support ANSI codes (rare on modern systems).

---

## Phase 2: Box and Table Utilities

**File:** `cli_colors.py` (add to existing)

**Goal:** Create functions for drawing bordered boxes and formatted tables

### Box Drawing Characters

Unicode has special characters for drawing boxes:

```
┌───────────────────┐
│ Content goes here │
└───────────────────┘
```

### Code to Add

```python
class BoxChars:
    """Unicode box-drawing characters."""
    TOP_LEFT =        '┌'
    TOP_RIGHT =       '┐'
    BOTTOM_LEFT =     '└'
    BOTTOM_RIGHT =    '┘'
    HORIZONTAL =      '─'
    VERTICAL =        '│'
    T_DOWN =          '┬'
    T_UP =            '┴'
    T_RIGHT =         '├'
    T_LEFT =          '┤'
    CROSS =           '┼'


def draw_box(title, content_lines, width=50):
    """
    Draw a box around content with optional title.

    Args:
        title: Text to show in top border (or None)
        content_lines: List of strings to display inside
        width: Total box width

    Returns:
        Complete box as string
    """
    lines = []
    inner_width = width - 2  # Account for left/right borders

    # Top border (alright i am going to have to find out some more about this, I will copy it for now,
    # but I must admit, I don't know entirely what all is going on here lol, oh well, pitter patter!
    if title:
        title_text = f" {title} "
        left_pad = (inner_width - len(title_text)) // 2
        right_pad = inner_width - len(title_text) - left_pad
        top = BoxChars.TOP_LEFT + (BoxChars.HORIZONTAL * left_pad) + title_text + (BoxChars.HORIZONTAL * right_pad) + BoxChars.TOP_RIGHT
    else:
        top = BoxChars.TOP_LEFT + (BoxChars.HORIZONTAL * inner_width) + BoxChars.TOP_RIGHT
    lines.append(colorize(top, Colors.CYAN))

    # Content lines
    for line in content_lines:
        padded = line.ljust(inner_width - 2)  # -2 for spacing
        row = f"{colorize(BoxChars.VERTICAL, Colors.CYAN)} {padded} {colorize(BoxChars.VERTICAL, Colors.CYAN)}"
        lines.append(row)

    # Bottom border
    bottom = BoxChars.BOTTOM_LEFT + (BoxChars.HORIZONTAL * inner_width) + BoxChars.BOTTOM_RIGHT
    lines.append(colorize(bottom, Colors.CYAN))

    return '\n'.join(lines)


def draw_table(headers, rows):
    """
    Draw a formatted table with headers and data rows.

    Args:
        headers: List of column header strings
        rows: List of tuples/lists containing row data

    Returns:
        Complete table as string
    """
    # Calculate column widths
    widths = []
    for i, header in enumerate(headers):
        max_width = len(header)
        for row in rows:
            if i < len(row):
                max_width = max(max_width, len(str(row[i])))
        widths.append(max_width + 2)  # +2 for padding

    lines = []

    # Top border
    top = BoxChars.TOP_LEFT
    for i, w in enumerate(widths):
        top += BoxChars.HORIZONTAL * w
        top += BoxChars.T_DOWN if i < len(widths) - 1 else BoxChars.TOP_RIGHT
    lines.append(colorize(top, Colors.CYAN))

    # Header row
    header_line = colorize(BoxChars.VERTICAL, Colors.CYAN)
    for header, w in zip(headers, widths):
        header_line += colorize(f" {header.ljust(w - 1)}", Colors.CYAN + Colors.BOLD)
        header_line += colorize(BoxChars.VERTICAL, Colors.CYAN)
    lines.append(header_line)

    # Header separator
    sep = BoxChars.T_RIGHT
    for i, w in enumerate(widths):
        sep += BoxChars.HORIZONTAL * w
        sep += BoxChars.CROSS if i < len(widths) - 1 else BoxChars.T_LEFT
    lines.append(colorize(sep, Colors.CYAN))

    # Data rows
    for row in rows:
        row_line = colorize(BoxChars.VERTICAL, Colors.CYAN)
        for cell, w in zip(row, widths):
            row_line += f" {str(cell).ljust(w - 1)}"
            row_line += colorize(BoxChars.VERTICAL, Colors.CYAN)
        lines.append(row_line)

    # Bottom border
    bottom = BoxChars.BOTTOM_LEFT
    for i, w in enumerate(widths):
        bottom += BoxChars.HORIZONTAL * w
        bottom += BoxChars.T_UP if i < len(widths) - 1 else BoxChars.BOTTOM_RIGHT
    lines.append(colorize(bottom, Colors.CYAN))

    return '\n'.join(lines)
```

### Test Code (update the test section)

```python
if __name__ == "__main__":
    # Colors
    print(error("[ERROR] Red"))
    print(success("[SUCCESS] Green"))
    print()

    # Box
    print(draw_box("My Box", ["Line one", "Line two", "Line three"]))
    print()

    # Table
    print(draw_table(
        ["Account", "Username", "Created"],
        [
            ("Gmail", "user@gmail.com", "2024-12-01"),
            ("Twitter", "tweeter123", "2024-12-15"),
        ]
    ))
```

---

## Phase 3: Fix Option 2 Bug (Generate Password)

**File:** `cli.py`

**Problem:** Option 2 duplicates Option 1's logic instead of calling `generate_password()`

### Replace `elif choice == "2":` block with:

```python
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

    # THIS is the key difference - generate instead of manual input
    print("[INFO] Let's generate a password...")
    password = generate_password()

    if manager.add_password(account, username, password):
        print(f"[SUCCESS] Password generated and saved!")
        print(f"[INFO] Your password: {password}")
        manager.save_to_file()
    else:
        print("[ERROR] Account already exists!")
```

---

## Phase 4: Fix Option 6 Bug (Delete Password)

**File:** `cli.py`

**Problems:**
- Missing `break` inside validation loop
- Stray `break` outside loop exits entire program
- No feedback on success/failure

### Replace `elif choice == "6":` block with:

```python
elif choice == "6":
    while True:
        dead_account_walking = input("Enter the account to delete: ").strip()
        if not dead_account_walking:
            print("Really Bro? Enter something!")
            continue
        break  # THIS break exits the input loop

    if manager.delete_password(dead_account_walking):
        print(f"[SUCCESS] '{dead_account_walking}' deleted!")
    else:
        print(f"[ERROR] '{dead_account_walking}' not found!")

    # NO break here - stay in menu
```

---

## Phase 5: Add Colors to All Messages

**File:** `cli.py`

### Step 1: Add import at top

```python
from cli_colors import error, success, warning, info, draw_box, draw_table
```

### Step 2: Wrap all print statements

Find and replace pattern:

| Before | After |
|--------|-------|
| `print("[ERROR] ...")` | `print(error("[ERROR] ..."))` |   
| `print("[SUCCESS] ...")` | `print(success("[SUCCESS] ..."))` |
| `print("[INFO] ...")` for success | `print(success("[SUCCESS] ..."))` |
| `print("[INFO] ...")` for neutral | `print(info("[INFO] ..."))` |
| `print("Really Bro? ...")` | `print(warning("Really Bro? ..."))` |

---

## Phase 6: Enhance Menu Display

**File:** `cli.py`

### Replace `display_menu()` function:

```python
def display_menu():
    from cli_colors import draw_box

    menu_items = [
        "1. Add new password (manual)",
        "2. Generate new password",
        "3. View password",
        "4. List all accounts",
        "5. Update password",
        "6. Delete password",
        "7. Quit"
    ]

    print("\n" + draw_box("Password Manager", menu_items, width=45))
```

---

## Phase 7: Table for Password List

**File:** `cli.py`

### Replace `elif choice == "4":` block:

```python
elif choice == "4":
    if len(manager.passwords) == 0:
        print(warning("No passwords saved yet!"))
    else:
        headers = ["Account", "Username", "Created"]
        rows = [(p.account, p.username, p.created_date) for p in manager.passwords]
        print("\n" + draw_table(headers, rows) + "\n")
```

---

## Phase 8: Box for Password View

**File:** `cli.py`

### Update the viewing section in Option 3:

After `pwd_obj = manager.get_password(account)`:

```python
if pwd_obj:
    content = [
        f"Account:  {pwd_obj.account}",
        f"Username: {pwd_obj.username}",
        f"Password: {pwd_obj.password}",
        f"Created:  {pwd_obj.created_date}"
    ]
    print("\n" + draw_box(f"Details: {pwd_obj.account}", content, width=45) + "\n")
else:
    print(error(f"[ERROR] '{account}' not found!"))
```

---

## Testing Checklist

### After Phase 1-2
- [ ] Run `python cli_colors.py`
- [ ] See colored output
- [ ] See box with border
- [ ] See table with columns

### After Phase 3
- [ ] Option 2 asks for account/username only
- [ ] Option 2 prompts for password generation options
- [ ] Generated password displays

### After Phase 4
- [ ] Option 6 deletes and shows success
- [ ] Option 6 shows error for non-existent account
- [ ] Program stays in menu after delete

### After Phase 5-8
- [ ] All errors show in red
- [ ] All successes show in green
- [ ] Menu has box border
- [ ] Password list shows as table
- [ ] Individual password view has box

---

## Quick Reference: What Goes Where

| Phase | File | What You're Doing |
|-------|------|-------------------|
| 1 | cli_colors.py | Create Colors class, color functions |
| 2 | cli_colors.py | Add BoxChars class, draw_box, draw_table |
| 3 | cli.py | Fix Option 2 to call generate_password() |
| 4 | cli.py | Fix Option 6 break/feedback issues |
| 5 | cli.py | Import colors, wrap all print statements |
| 6 | cli.py | Replace display_menu() with box version |
| 7 | cli.py | Replace Option 4 with table version |
| 8 | cli.py | Replace Option 3 view with box version |

---

## Concepts You'll Learn

1. **ANSI Escape Codes** - How `\033[91m` becomes red text
2. **Unicode Box Drawing** - Using `┌`, `─`, `│`, etc.
3. **String Padding** - `.ljust()` for alignment
4. **List Comprehensions** - `[(p.account, p.username) for p in passwords]`
5. **Function Composition** - Small utilities building bigger features
