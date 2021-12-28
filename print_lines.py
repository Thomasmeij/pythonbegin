

def print_stars_line_length_ten():
    """Print een horizontale lijn van 10 sterren."""
    print(10*"*")

def print_stars_line(length):
    """Print een horizontale lijn van `length` aantal sterren."""
    line = '*' * length
    print(line)

def print_line(length, character):
    """Print een horizontale lijn van length aantal characters. """
    line = character * length
    print(line)

def main():
    line_length = 25

    print_stars_line_length_ten()
    print_stars_line(line_length)
    print_stars_line(line_length + 5)

    char = '#'
    print_line(line_length, character="%")
    print_line(length=line_length, character=char)


if __name__ == "__main__":
    main()