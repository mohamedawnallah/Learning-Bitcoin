import base58

text = "Hello World!"
base58_string_encoded = base58.b58encode(text.encode("utf-8").decode("utf-8"))
print(base58_string_encoded)

base58_string_decoded = base58.b58decode(base58_string_encoded).decode("utf-8")
print(base58_string_decoded)