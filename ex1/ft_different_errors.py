


def garden_operations() -> None:
    """
    Demonstrates various error types that can occur in garden operations.
    """
    print("=== Garden Error Types Demo ===")
    
    # Testing ValueError
    print("\nTesting ValueError...")
    try:
        plant_count = int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    
    # Testing ZeroDivisionError
    print("\nTesting ZeroDivisionError...")
    try:
        plants_per_row = 10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    
    # Testing FileNotFoundError
    print("\nTesting FileNotFoundError...")
    try:
        with open("missing.txt", "r") as file:
            content = file.read()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: No such file 'missing.txt'")
    
    # Testing KeyError
    print("\nTesting KeyError...")
    try:
        garden_plants = {"tomato": 5, "lettuce": 3}
        count = garden_plants["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}")


def test_error_types() -> None:
    """
    Tests different error types and demonstrates catching multiple errors.
    """
    garden_operations()
    
    # Testing multiple errors together
    print("\nTesting multiple errors together...")
    
def op_value_error():
    int("not_a_number")


def op_zero_division():
    5 / 0


def op_file_not_found():
    open("nonexistent.txt", "r")


def op_key_error():
    {"key": "value"}["missing"]


def test_error_types() -> None:
    """
    Tests different error types and demonstrates catching multiple errors.
    """
    garden_operations()

    print("\nTesting multiple errors together...")

    test_operations = [
        op_value_error,
        op_zero_division,
        op_file_not_found,
        op_key_error
    ]

    for operation in test_operations:
        try:
            operation()
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
            print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()

