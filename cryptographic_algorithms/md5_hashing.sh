#!/bin/bash
file=$1

hash=$(md5sum "$file" | cut -d ' ' -f 1)

echo "$hash"