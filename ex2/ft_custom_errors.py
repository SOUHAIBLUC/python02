"""
Exercise 2: Making Your Own Error Types
Demonstrates creating custom exception classes for garden-specific errors
"""


class GardenError(Exception):
    """Base exception class for garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-related problems."""
    pass


class WaterError(GardenError):
    """Exception raised for watering-related problems."""
    pass


def check_plant_status(plant_name: str) -> None:
    """
    Checks plant status and raises PlantError if wilting.
    
    Args:
        plant_name: Name of the plant to check
        
    Raises:
        PlantError: If plant is wilting
    """
    raise PlantError(f"The {plant_name} plant is wilting!")


def check_water_level(tank_level: int) -> None:
    """
    Checks water tank level and raises WaterError if insufficient.
    
    Args:
        tank_level: Current water level in tank
        
    Raises:
        WaterError: If water level is too low
    """
    if tank_level < 20:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    """
    Demonstrates custom error types and hierarchical exception handling.
    """
    print("=== Custom Garden Errors Demo ===")
    
    # Testing PlantError
    print("\nTesting PlantError...")
    try:
        check_plant_status("tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    
    # Testing WaterError
    print("\nTesting WaterError...")
    try:
        check_water_level(10)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    
    # Testing catching all garden errors
    print("\nTesting catching all garden errors...")
    
    try:
        check_plant_status("tomato")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    
    try:
        check_water_level(5)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
