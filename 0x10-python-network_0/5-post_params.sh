#!/bin/bash
# Script that takes a URL, sends a POST request and displays the body of the response
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will allways be here for PLD" "$1"
