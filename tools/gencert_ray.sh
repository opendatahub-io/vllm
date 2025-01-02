#!/bin/sh
## Create tls.key
openssl genrsa -out /etc/ray/tls/tls.key 2048

## Write CSR Config
cat > /etc/ray/tls/csr.conf <<EOF
[ req ]
default_bits = 2048
prompt = no
default_md = sha256
req_extensions = req_ext
distinguished_name = dn

[ dn ]
C = US
ST = Raleigh
L = North Carolina
O = redhat
OU = redhat
CN = self-signed-cert

[ req_ext ]
subjectAltName = @alt_names

[ alt_names ]
DNS.1 = localhost
DNS.2 = *.${POD_NAMESPACE}.svc.cluster.local
IP.1 = 127.0.0.1
IP.2 = $POD_IP

EOF

## Create CSR using tls.key
openssl req -new -key /etc/ray/tls/tls.key -out /etc/ray/tls/ca.csr -config /etc/ray/tls/csr.conf

## Write cert config
cat > /etc/ray/tls/cert.conf <<EOF

authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names

[alt_names]
DNS.1 = localhost
DNS.2 = *.${POD_NAMESPACE}.svc.cluster.local
IP.1 = 127.0.0.1
IP.2 = $POD_IP

EOF

## create serial file
echo '01' > /tmp/ca.srl

## Generate tls.cert
openssl x509 -req \
    -in /etc/ray/tls/ca.csr \
    -CA /etc/ca/tls/tls.crt -CAkey /etc/ca/tls/tls.key \
    -CAserial /tmp/ca.srl  -out /etc/ray/tls/tls.crt \
    -days 3650 \
    -sha256 -extfile /etc/ray/tls/cert.conf

