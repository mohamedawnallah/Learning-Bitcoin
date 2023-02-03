from ecdsa import SigningKey, SECP256k1


message = "Not your keys, not your coins!".encode("utf-8")

sk = SigningKey.generate(curve=SECP256k1)
vk = sk.verifying_key
signature = sk.sign(message)
print(signature)

assert vk.verify(signature, b"Not your keys, not your coins!")

print("If your script runs to this point without an error, congrats, you successfully validated the signature!")