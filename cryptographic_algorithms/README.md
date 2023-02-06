# Difference between Symmetric and Asymmetric Encryption

## symmetric_encryption bash script
### Overview
This script provides a basic implementation of symmetric encryption and decryption using the `openssl` command-line tool. The script will check if openssl is installed, generate a random symmetric key, use this key to encrypt and decrypt a specified plaintext file, and then compare the decrypted data with the original plaintext to confirm that the encryption and decryption process was successful.

### Requirements
The `openssl` command-line tool must be installed on the system running this script.

### Usage
The script takes four arguments, in the following order:

- `plaintext_file`: the file that contains the plaintext data to be encrypted
- `encrypted_file`: the file to which the encrypted data will be written
- `decrypted_file`: the file to which the decrypted data will be written
- `key_file`: the file to which the symmetric key will be written

Example usage:
```bash
./symmetric-encryption-script.sh data/plaintext.txt data/ncrypted.txt data/decrypted.txt sample_keys/secret.key
```

### Output
The script will generate the following output:

- If `openssl` is not installed, an error message indicating this will be displayed and the script will exit with a return code of 1.
-If the number of arguments provided is not 4, a usage message will be displayed and the script will exit with a return code of 1.
- If the encryption and decryption process was successful, a success message indicating that the decrypted data matches the original plaintext will be displayed.
- If the encryption and decryption process was not successful, an error message indicating that the decrypted data does not match the original plaintext will be displayed and the script will exit with a return code of 1.

### Note
This script provides a basic implementation of symmetric encryption and decryption, and is intended to demonstrate the use of the `openssl` tool. It should not be used in a production environment without appropriate modification and testing to ensure that it meets the specific requirements of the intended use case.

## asymmetric_encryption python script
This is a sample script that demonstrates the use of RSA cryptography and hashlib in Python. The script performs the following steps:
- Generate a 1024-bit RSA private and public key pair using the RSA.generate() method.
- Convert the private and public keys to PEM format and write them to disk as "private.pem" and "public.pem" files, respectively.
- Read the PEM-formatted private and public keys from disk and import them using the `RSA.import_key()` method.
- Encrypt the message `I love cryptography!` using the public key and the PKCS1_OAEP cipher for the purpose of data security.
- Hash the plaintext message using the SHA256 algorithm for the purpose of data integrity
- Transmit the encrypted message and the hashed message to the receiver.
- Decrypt the received encrypted message using the private key.
- Hash the received decrypted message and compare it to the received hashed message.
- If the two hashed messages match, the message is considered authentic. Otherwise, it is considered tampered with.

The script uses the following libraries:
- hashlib for computing SHA256 hashes
- Crypto.Cipher for performing encryption and decryption using PKCS1_OAEP
- Crypto.PublicKey for generating and importing RSA keys.

# Use Cases of Asymmetric Encryption
- `Public Key Infrastructure (PKI)` the public key is used for encryption
   and the private key for decryption
- `Digital Signature` The owner of key pairs(public,private) signs data using private key and anyone who has the public key may verify this signature (Encryption(public_key,private_key) + Hashing = Digital Signature)
# Encryption vs Encoding vs Hashing Algorithms
- Encryption is Reversible, hashing's irreversible (One-way)
- Encoding is the process of representing data in a form that’s convenient for people or computers to work with for example
there is Base64, UTF-8, ASCII system encoding
- Usually Encryption is used with secure encoded data
- Ususally Hashing don't require any key: `Data -> Hashing Function -> Hash` but there are some hashing functions add keys
# Encryption Algorithms
- Symmetric:
    - DES -> 56bits (obsolete as it's vulnerable to attacks)
    - 3DES -> 112bits (obsolete as it's vulnerable to attacks)
    - AES (Advanced Encryption System) -> utilizes different length of bits (e.g: 128, 256) **Recommended** it is also used
      SSL communication in HTTPs protocol 
- Asymmetric:
    - RSA (`Public key crypto system`) -> (1024, 2048, 3072, 4096 bits)
# Hashing Algorithms
- MD5 -> 128 bit variable length
- SHA -> SHA-1 (160bit), SHA-256(256bit), SHA-512(512bit) 
- HMAC -> Usually used with MD5 and SHA, It add a secret key to the hashing process (Data + Key = Hash) with another level of security.
# How RSA Protocol works

# What is Public Key Infrastructure ?
Wikipedia said "A public key infrastructure (PKI) is a set of roles, policies, hardware, software and procedures needed to create, manage, distribute, use, store and revoke digital certificates and manage public-key encryption." So it's based on trust

# Hashing Algorithms (sha, md5) and How they are used in public key infrastructure

# What are Signature Hash Types (SIGHASH) ?

# The Importance of Randomness in Signatures

# What is Deterministic Random Seed

# What is Locking Script and Unlocking Script
![Locking and Unlocking Script](assets/locking%20and%20unlocking%20script.png)
# What is Pay to Public Key Hash Script

