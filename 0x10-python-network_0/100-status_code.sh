#!/bin/bash
# send a URL request and display status code of the response
curl -sI -w '%{response_code}' "$1" -o /dev/null
