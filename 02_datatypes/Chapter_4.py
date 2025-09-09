is_boiling = True
stir_count = 5
total_actions = stir_count + is_boiling
print(f"Total actions: {total_actions}")

water_hot = True
tea_added = True

can_server = water_hot and tea_added
print(f"Answer: {can_server}")