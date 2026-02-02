"""
Exercise 3: Finally Block - Always Clean Up
Demonstrates using finally blocks for resource cleanup
"""


def water_plants(plant_list: list) -> None:
    """
    Waters a list of plants, ensuring cleanup happens regardless of errors.
    
    Args:
        plant_list: List of plant names to water
        
    Raises:
        ValueError: If a plant name is invalid (None or empty)
    """
    print("Opening watering system")
    
    try:
        for plant in plant_list:
            if plant is None or plant == "":
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """
    Demonstrates finally block behavior with normal and error scenarios.
    """
    print("=== Garden Watering System ===")
    
    # Testing normal watering
    print("\nTesting normal watering...")
    try:
        water_plants(["tomato", "lettuce", "carrots"])
        print("Watering completed successfully!")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Testing with error
    print("\nTesting with error...")
    try:
        water_plants(["tomato", None, "carrots"])
        print("Watering completed successfully!")
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
