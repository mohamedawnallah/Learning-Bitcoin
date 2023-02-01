#!/bin/bash

# Check if openssl is installed
if ! command -v openssl > /dev/null 2>&1; then
  echo "Error: openssl is not installed"
  exit 1
fi

# Check number of arguments
if [ $# -ne 4 ]; then
  echo "Usage: $0 plaintext_file encrypted_file decrypted_file secret_key"
  exit 1
fi

# File names
plaintext_file=$1
encrypted_file=$2
decrypted_file=$3
key_file=$4

# Generate symmetric key
openssl rand -base64 32 > "$key_file"

# Encrypt data
openssl enc -aes-256-cbc -salt -in "$plaintext_file" -out "$encrypted_file" -k "$(cat $key_file)"

# Decrypt data
openssl enc -d -aes-256-cbc -in "$encrypted_file" -out "$decrypted_file" -k "$(cat $key_file)"

# Confirm decrypted data matches original plaintext
if cmp -s "$plaintext_file" "$decrypted_file"; then
  echo "Success: decrypted data matches original plaintext"
else
  echo "Error: decrypted data does not match original plaintext"
  exit 1
fi

