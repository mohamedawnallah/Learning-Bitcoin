from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

message = 'I love cryptography!'.encode("utf-8")

private_key = RSA.generate(1024)
public_key = private_key.publickey()

print(type(private_key), type(public_key))

private_pem = private_key.export_key().decode()
public_pem = public_key.export_key().decode()

print(type(private_pem), type(public_pem))

with open("sample_keys/private.pem", "w") as private_fh:
	private_fh.write(private_pem)

with open("sample_keys/public.pem", "w") as public_fh:
	public_fh.write(public_pem)

print("private.pem:")
with open("sample_keys/private.pem", "r") as private_fh:
	private_key_data = private_fh.read()
	print(private_key_data)

print("public.pem:")
with open("sample_keys/public.pem", "r") as public_fh:
	public_key_data = public_fh.read()
	print(public_key_data)

private_key = RSA.import_key(private_key_data)
public_key = RSA.import_key(public_key_data)

print(type(private_key), type(public_key))

cipher = PKCS1_OAEP.new(key=public_key)
cipher_text = cipher.encrypt(message)

print(cipher_text)

decrypt = PKCS1_OAEP.new(key=private_key)
decrypted_message = decrypt.decrypt(cipher_text)

print(decrypted_message)

print("Done!")
