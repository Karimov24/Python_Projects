class ShippingCalculator:
    def __init__(self, weight):
        self.weight = weight

    def calculate_ground_shipping(self):
        if self.weight <= 2:
            cost_ground = self.weight * 1.5 + 20
        elif self.weight <= 6:
            cost_ground = self.weight * 3.00 + 20
        elif self.weight <= 10:
            cost_ground = self.weight * 4.00 + 20
        else:
            cost_ground = self.weight * 4.75 + 20
        return cost_ground

    def calculate_drone_shipping(self):
        if self.weight <= 2:
            cost_drone = self.weight * 4.50
        elif self.weight <= 6:
            cost_drone = self.weight * 9.00
        elif self.weight <= 10:
            cost_drone = self.weight * 12.00
        else:
            cost_drone = self.weight * 14.25
        return cost_drone

    def calculate_premium_ground_shipping(self):
        return 125.00

# Example usage:
weight = 5.5  # Adjust weight as needed
calculator = ShippingCalculator(weight)

cost_ground = calculator.calculate_ground_shipping()
print(f"Ground Shipping: ${cost_ground:.2f}")

cost_drone = calculator.calculate_drone_shipping()
print(f"Drone Shipping: ${cost_drone:.2f}")

cost_premium_ground = calculator.calculate_premium_ground_shipping()
print(f"Premium Ground Shipping: ${cost_premium_ground:.2f}")
