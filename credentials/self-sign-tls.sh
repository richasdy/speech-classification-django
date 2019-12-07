#!/bin/sh

# generate private key and enter pass phrase
openssl genrsa -des3 -out private_key.pem 2048 # must have pass phrase
openssl genrsa -out private_key.pem 2048 # without pass phrase

# create certificate signing request, enter "*.example.com" as a "Common Name", leave "challenge password" blank
openssl req -new -sha256 -key private_key.pem -out server.csr

# generate self-signed certificate for 1 year
openssl req -x509 -sha256 -days 365 -key private_key.pem -in server.csr -out server.pem

# validate the certificate
openssl req -in server.csr -text -noout | grep -i "Signature.*SHA256" && echo "All is well" || echo "This certificate doesn't work in 2017! You must update OpenSSL to generate a widely-compatible certificate"
 
#--------------------------------------------------------------------------------#

# generate self-signed certificate for 1 year without key pass phrase, certificate signing request and challenge password
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
