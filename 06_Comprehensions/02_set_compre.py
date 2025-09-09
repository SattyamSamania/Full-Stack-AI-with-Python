favourite_chais = [
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elachi Chai"
]

unique_chai = {chai for chai in favourite_chais if len(chai) >9}
print(unique_chai)