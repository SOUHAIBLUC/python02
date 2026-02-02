"""
Exercise 5: Garden Management System
Integrates all error handling techniques into a complete system
"""


class GardenError(Exception):
    """Base exception for garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception for plant-related problems."""
    pass


class WaterError(GardenError):
    """Exception for watering-related problems."""
    pass


class GardenManager:
    """Manages garden operations with comprehensive error handling."""
    
    def __init__(self) -> None:
        """Initialize garden manager with empty plant dictionary."""
        self.plants: dict = {}
        self.water_tank: int = 100
    
    def add_plant(self, plant_name: str, water_level: int = 5,
                  sunlight_hours: int = 8) -> None:
        """
        Adds a plant to the garden with validation.
        
        Args:
            plant_name: Name of the plant
            water_level: Initial water level (1-10)
            sunlight_hours: Daily sunlight hours (2-12)
            
        Raises:
            ValueError: If plant name is empty or parameters are invalid
        """
        if not plant_name or plant_name == "":
            raise ValueError("Plant name cannot be empty!")
        
        if water_level < 1 or water_level > 10:
            raise ValueError(f"Water level must be between 1 and 10")
        
        if sunlight_hours < 2 or sunlight_hours > 12:
            raise ValueError(f"Sunlight hours must be between 2 and 12")
        
        self.plants[plant_name] = {
            "water": water_level,
            "sun": sunlight_hours
        }
        print(f"Added {plant_name} successfully")
    
    def water_plants(self) -> None:
        """
        Waters all plants in the garden with proper cleanup.
        
        Raises:
            WaterError: If water tank is empty
        """
        print("\nWatering plants...")
        
        if self.water_tank < 10:
            raise WaterError("Not enough water in tank")
        
        print("Opening watering system")
        
        try:
            for plant_name in self.plants:
                print(f"Watering {plant_name} - success")
                self.water_tank -= 5
        finally:
            print("Closing watering system (cleanup)")
    
    def check_plant_health(self, plant_name: str) -> None:
        """
        Checks and displays plant health status.
        
        Args:
            plant_name: Name of the plant to check
            
        Raises:
            PlantError: If plant doesn't exist
            ValueError: If plant parameters are invalid
        """
        if plant_name not in self.plants:
            raise PlantError(f"Plant '{plant_name}' not found in garden")
        
        plant = self.plants[plant_name]
        water = plant["water"]
        sun = plant["sun"]
        
        if water > 10:
            raise ValueError(f"Water level {water} is too high (max 10)")
        
        if sun < 2 or sun > 12:
            raise ValueError(f"Sunlight hours {sun} out of range (2-12)")
        
        print(f"{plant_name}: healthy (water: {water}, sun: {sun})")


def test_garden_management() -> None:
    """
    Demonstrates comprehensive garden management with error handling.
    """
    print("=== Garden Management System ===")
    
    garden = GardenManager()
    
    # Adding plants
    print("\nAdding plants to garden...")
    try:
        garden.add_plant("tomato", 5, 8)
        garden.add_plant("lettuce", 6, 6)
        garden.add_plant("", 5, 8)  # This will fail
    except ValueError as e:
        print(f"Error adding plant: {e}")
    
    # Watering plants
    try:
        garden.water_plants()
    except WaterError as e:
        print(f"Error watering: {e}")
    
    # Checking plant health
    print("\nChecking plant health...")
    try:
        garden.check_plant_health("tomato")
    except (PlantError, ValueError) as e:
        print(f"Error checking tomato: {e}")
    
    # Manually set bad water level to test validation
    garden.plants["lettuce"]["water"] = 15
    
    try:
        garden.check_plant_health("lettuce")
    except (PlantError, ValueError) as e:
        print(f"Error checking lettuce: {e}")
    
    # Testing error recovery
    print("\nTesting error recovery...")
    garden.water_tank = 5  # Set low water
    
    try:
        garden.water_plants()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")
    
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
