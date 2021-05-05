#!/bin/bash
# Script that takes a URL and sends back a request to it
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
