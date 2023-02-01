# Difference between Symmetric and Asymmetric Encryption

## symmetric_encryption script
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

## asymmetric_encryption script

# Encryption vs Encoding vs Hashing Algorithms
- Encryption is Reversible, hashing not (One-way)
- Encoding is the process of representing data in a form that’s convenient for people or computers to work with for example
there is Base64, UTF-8, ASCII system encoding
- Usually Encryption is used with secure encoded data
# Encryption Algorithms
- Symmetric:
    - DES -> 56bits (obsolete as it's vulnerable to attacks)
    - 3DES -> 112bits (obsolete as it's vulnerable to attacks)
    - AES (Advanced Encryption System) -> utilizes different length of bits (e.g: 128, 256) **Recommended** it is also used
      SSL communication in HTTPs protocol 
- Asymmetric:
    - RSA
# How RSA Protocol works

# What is Public Key Infrastructure ?

# Hashing Algorithms (sha, md5) and How they are used in public key infrastructure
