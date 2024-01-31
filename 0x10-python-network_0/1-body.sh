#!/usr/bin/env bash
# This script takes in a URL,
# sends a GET request to the URL,
# and displays the body of the response only if the status code is 200

status=$(curl -sLI $1 | grep '200 OK' | awk '{print $2}')
if [ $status == 200 ]; then
	curl -sL $1
fi
