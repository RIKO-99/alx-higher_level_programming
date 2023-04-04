#!/bin/bash

# Get URL from user input
read -p "Enter URL: " url

# Send request and get response size in bytes
response=$(curl -s -w "%{size_download}" -o /dev/null $url)

# Display response size
echo "Response size in bytes: $response"

