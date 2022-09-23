#!/bin/bash
# send a GET request to a URL and display the body
curl -s "$1" -X GET -H "X-School-User-Id: 98"
