weight = 41.5  # Corrected the typo here

# Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:  # Corrected the condition to correctly capture weights > 2 and <= 6
  cost_ground = weight * 3.00 + 20
elif weight <= 10:  # Corrected the condition to correctly capture weights > 6 and <= 10
  cost_ground = weight * 4.00 + 20
else:  # Removed the condition for the else statement
  cost_ground = weight * 4.75 + 20

print(cost_ground)
cost_ground_premium = 125.00
print("Ground Shipping Premium $", cost_ground_premium)


#Drone Shipping
if weight <= 2:
  cost_ground = weight * 4.50 + 0
elif weight <=6:
  cost_ground = weight * 9.00 + 0
elif weight <=10:
  cost_ground = weight * 12.00 + 0
else:
  cost_ground = weight * 14.25 + 0

print(cost_ground)
cost_ground_premium = 125.00
print("Consider your own choice!!!")