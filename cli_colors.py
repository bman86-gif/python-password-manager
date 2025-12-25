#  this is for the kickass looking cli application for my custom password manager, more to come!
#  cli_colors.py

class Colors:
    """ANSI color codes for terminal output"""
    # Text colors (bright versions: 90-97)
    RED       = "\033[91m"
    GREEN     = "\033[92m"
    YELLOW    = "\033[93m"
    BLUE      = "\033[94m"
    MAGENTA   = "\033[95m"
    CYAN      = "\033[96m"
    WHITE     = "\033[97m"
    GRAY      = "\033[98m"
    #Styles
    BOLD      = "\033[1m"
    UNDERLINE = "\033[4m"
    # Reset
    RESET     = "\033[0m"


class BoxChars:
    """Unicode box-drawing characters"""
    TOP_LEFT     = '┌'
    TOP_RIGHT    = '┐'
    BOTTOM_LEFT  = '└'
    BOTTOM_RIGHT = '┘'
    HORIZONTAL   = '─'
    VERTICAL     = '│'
    T_DOWN       = '┬'
    T_UP         = '┴'
    T_RIGHT      = '├'
    T_LEFT       = '┤'
    CROSS        = '┼'

def colorize(text, color):
    """Wrap text with color code and reset"""
    return f"{color}{text}{Colors.RESET}"
def error(text):
    """Red text for errors"""
    return colorize(text, Colors.RED)
def success(text):
    """Green text for success messages"""
    return colorize(text, Colors.GREEN)
def warning(text):
    """Yellow text for warnings."""
    return colorize(text, Colors.YELLOW)
def info(text):
    """Blue text for info."""
    return colorize(text, Colors.BLUE)
def heading(text):
    """Cyan bold text for headings."""
    return colorize(text, Colors.CYAN + Colors.BOLD)
def draw_box(title, content_lines, width=50):
    """
    draw a box around content with optional title.
    :param title:
    :param content_lines:
    :param width:
    :return:
        complete box as string
    """
    lines = []
    inner_width = width - 2 # accounting for left and right corners
    if title:
        title_text = f" {title} "
        left_pad   = (inner_width - len(title_text)) // 2
        right_pad  = inner_width - len(title_text) - left_pad
        top        = BoxChars.TOP_LEFT + (BoxChars.HORIZONTAL * left_pad) + title_text + (BoxChars.HORIZONTAL * right_pad) + BoxChars.TOP_RIGHT
    else:
        top        = BoxChars.TOP_LEFT + (BoxChars.HORIZONTAL * inner_width) + BoxChars.TOP_RIGHT
    lines.append(colorize(top, Colors.CYAN))


    # Content lines
    for line in content_lines:
        padded = line.ljust(inner_width - 2) #  -2 for spacing
        row    = f"{colorize(BoxChars.VERTICAL, Colors.CYAN)} {padded} {colorize(BoxChars.VERTICAL, Colors.CYAN)}"
        lines.append(row)

    #  Bottom border
    bottom = BoxChars.BOTTOM_LEFT + (BoxChars.HORIZONTAL * inner_width) + BoxChars.BOTTOM_RIGHT
    lines.append(colorize(bottom, Colors.CYAN))

    return '\n'.join(lines)
def draw_table(headers, rows):
    # calculate column widths
    widths = []
    for i, header in enumerate(headers):
        max_width = len(header)
        for row in rows:
            if i < len(row):
                max_width = max(max_width,len(str(row[i])))
        widths.append(max_width + 2) # +2 for padding

    lines =[]

    # Top Border
    top = BoxChars.TOP_LEFT
    for i, w in enumerate(widths):
        top += BoxChars.HORIZONTAL * w
        top += BoxChars.T_DOWN if i < len(widths) - 1 else BoxChars.TOP_RIGHT
    lines.append(colorize(top, Colors.CYAN))

    # Header row
    header_line = colorize(BoxChars.VERTICAL, Colors.CYAN)
    for header, w in zip(headers, widths):
        header_line += colorize(f" {header.ljust(w -1)}", Colors.CYAN + Colors.BOLD)
        header_line += colorize(BoxChars.VERTICAL,Colors.CYAN)
    lines.append(header_line)
    # Header seperator
    sep = BoxChars.T_RIGHT
    for i, w in enumerate(widths):
        sep += BoxChars.HORIZONTAL * w
        sep += BoxChars.CROSS if i < len(widths) - 1 else BoxChars.T_LEFT
    lines.append(colorize(sep, Colors.CYAN))

    #  Data rows
    for row in rows:
        row_line = colorize(BoxChars.VERTICAL, Colors.CYAN)
        for cell, w in zip(row, widths):
            row_line += f" {str(cell).ljust(w - 1)}"
            row_line += colorize(BoxChars.VERTICAL, Colors.CYAN)


    # Bottom border
    bottom = BoxChars.BOTTOM_LEFT
    for i, w in enumerate(widths):
        bottom = BoxChars.HORIZONTAL * w
        bottom = BoxChars.T_UP if i < len(widths) - 1 else BoxChars.BOTTOM_RIGHT
    lines.append(colorize(bottom, Colors.CYAN))


    return '\n'.join(lines)

if __name__ == "__main__":
    print(error("[ERROR] This should be RED"))
    print(success("[SUCCESS] This should be GREEN"))
    print(warning("[WARNING] This should be YELLOW"))
    print()
    print(info("[INFO] This should be BLUE"))
    print(heading("===HEADING==="))
    print(draw_box(
                "My Box",
        ["Line one",
                    "Line two",
                    "Line three"]))
    print()
    print(draw_table(
        ["Account", "Username", "Created"],
        [
            ("Gmail", "user@gmail.com", "2024-12-01"),
            ("Twitter", "tweeter123", "2024-12-15"),

        ]
    ))












