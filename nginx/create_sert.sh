#!/bin/bash

mkdir -p ./ssl

openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout ./ssl/local.key \
    -out ./ssl/local.crt \
    -subj "/C=UA/ST=Kyiv/L=Kyiv/O=MyCompany/OU=Dev/CN=localhost"
