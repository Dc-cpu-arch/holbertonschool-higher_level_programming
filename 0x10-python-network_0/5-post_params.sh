#!/bin/bash
# Script that takes a URL, sends a POST request and displays the body of the response
curl -sd "email=hr@holbertonschool.com&subject=I%20will%20allways%20be%20here%20for%20PLD" "$1"
