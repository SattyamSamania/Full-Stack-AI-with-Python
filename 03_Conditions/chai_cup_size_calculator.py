cup_size = input("Enter your prefered cup size: ").lower()

if cup_size == "small":
    print(f"Price is 10 rupees.")
elif cup_size == "medium":
    print("Price is 15 rupees")
elif cup_size == "large":
    print("Price is 20 rupees")
else:
    print("Unknown cup size")    
        