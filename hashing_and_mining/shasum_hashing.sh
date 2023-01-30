#!/bin/bash

file=$1
hash_type=$2

if [ -z "$hash_type" ]; then
hash_type=256
fi

hash=$(shasum -a "$hash_type" "$file" | awk '{ print $1 }')

echo "The sha$hash_type hash of the contents of $file is: $hash"

