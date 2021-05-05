#!/bin/bash
# Script that takes a URL and displays all the HTTP methods the server will accept
curl -sI "$1" | grep "Allow" | cut -f2- -d" "
