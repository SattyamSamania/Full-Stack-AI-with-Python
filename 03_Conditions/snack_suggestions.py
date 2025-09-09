snack = input("Enter your prefered snack: ").lower()
print(f"user said: {snack}")

if snack == "cookies" or snack == "samosa":
    print(f"Great choice! We'll serve you {snack}")
else:
    print(f"Sorry, we cannot serve you {snack} this time! ")