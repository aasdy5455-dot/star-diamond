def draw_diamond(size: int) -> None:
    """Print a star diamond using nested loops."""
    if size < 1:
        raise ValueError("Size must be a positive integer.")

    # Upper half (including the middle row)
    for row in range(size):
        spaces = size - row - 1
        stars = 2 * row + 1
        for _ in range(spaces):
            print(" ", end="")
        for _ in range(stars):
            print("*", end="")
        print()

    # Lower half
    for row in range(size - 2, -1, -1):
        spaces = size - row - 1
        stars = 2 * row + 1
        for _ in range(spaces):
            print(" ", end="")
        for _ in range(stars):
            print("*", end="")
        print()


def main() -> None:
    try:
        size = int(input("Enter the diamond size (e.g. 5): "))
        draw_diamond(size)
    except ValueError as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
