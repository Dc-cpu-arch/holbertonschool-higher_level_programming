#!/bin/bash
# Scripts that sends a GET resquest to the URL and displays the body of the response
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" "$1"
