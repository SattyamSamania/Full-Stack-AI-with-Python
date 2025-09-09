chai_type = "Ginger Chai"
customer_name = "Sattyam"

print(F"Order for {customer_name} : {chai_type} please!")

chai_description = "Aromatic and Bold"
print(f"first word: {chai_description[0:8:2]}")
print(f"first word: {chai_description[::-1]}")

lable_text = "Chai Special"
encoded_label = lable_text.encode("utf-8")
print(f"Non Encoded label: {lable_text}")
print(f"Encoded lable: {encoded_label}")