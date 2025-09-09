chai_receipe = {}
chai_receipe["base"] = "black tea"
chai_receipe["liquid"] = "milk"

print(f"Receipe base:  {chai_receipe['base']}")

chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}
# print(f"Order details (keys): {chai_receipe.keys()}")

last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")