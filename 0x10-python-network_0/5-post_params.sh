#!/bin/bash
# send a POST request to argv[0] URL and display the body of the response
curl -s "$1" -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
