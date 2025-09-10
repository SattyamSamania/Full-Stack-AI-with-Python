class Chai:
    temperature = "hot"
    strength = "Strong"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "mild"
print(f"After changing: ",cutting.temperature)

del cutting.temperature
print(cutting.temperature)