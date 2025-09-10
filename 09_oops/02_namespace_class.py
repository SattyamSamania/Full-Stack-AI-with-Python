class Chai:
    origin = "India"

print(Chai.origin)   

Chai.is_hot = False
print(Chai.is_hot)

# creating objects from class CHai

masala = Chai()
print(f"Masala {masala.origin}")
print(f"Masala {masala.is_hot}")