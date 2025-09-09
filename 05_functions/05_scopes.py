def serve_chai():
    chai_type = "Masala" # local scope
    print(f"Inside function {chai_type}")


chai_type = "Lemon"
serve_chai()
print(f"Outside function: {chai_type}")


def chai_counter():
    chai_order = "lemon" # Enclosing scope
    def print_order():
        chai_order="Ginger"
        print("Inside function chai_order:", chai_order)
    print_order()
    print("Outer: ", chai_order)    

chai_counter()    