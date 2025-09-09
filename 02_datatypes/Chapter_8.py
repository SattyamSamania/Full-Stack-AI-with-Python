ingredients = ["water", "black_tea", "milk"]
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")


spice_options = ["cardamom", "ginger"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"merge: {chai_ingredients}")
chai_ingredients.insert(2, "black_tea")
print(f" {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"last added: {chai_ingredients}")

sugar_levels = [3,4,5,2,532,523,5345]
print(f"Maximum sugar level: {max(sugar_levels)}")
