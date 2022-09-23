#!/bin/bash
# Take a URL, send a GET request to the URL and display the body of the
# response
curl -s "$1" -X GET -L
