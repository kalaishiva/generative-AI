import tiktoken

# I want to create a token encoder for this particular model
enc = tiktoken.encoding_for_model("gpt-4o")


#text added
text = "Hi there! My name is Kalaivani"
tokens = enc.encode(text)

print("Tokens : ", tokens)
# output = Tokens [12194, 1354, 0, 3673, 1308, 382, 50151, 349, 3048]


decoded = enc.decode([12194, 1354, 0, 3673, 1308, 382, 50151, 349, 3048])
print("Decoded : ", decoded)
# output = Decoded :  Hi there! My name is Kalaivani