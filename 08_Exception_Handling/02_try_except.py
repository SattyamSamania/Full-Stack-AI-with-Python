chai_menu = {"masala": 30, "ginger": 60}

try:
    chai_menu["elaichi"]
except KeyError:
    print("The key that you are trying to access does not exists")    

def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError("We don't know that flavor")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavor} chai is sreved")
    finally:
        print("next customer please")    

serve_chai("masala")
serve_chai("unknown")
