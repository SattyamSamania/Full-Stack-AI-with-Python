import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Sattyam Samania"
tokens = encoder.encode(text)

# Tokens [25216, 3274, 0, 3673, 1308, 382, 22232, 1206, 313, 336, 7601, 535]
print("Encoded Tokens", tokens)

decoded = encoder.decode([25216, 3274, 0, 3673, 1308, 382, 22232, 1206, 313, 336, 7601, 535])
print("Decoded", decoded)
