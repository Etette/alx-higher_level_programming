#!/bin/bash
# make a request to 0.0.0.0:5000/catch_me that cause server to respond with 'you got me'
curl -s 0.0.0.0:5000/catch_me -X PUT -L -d "user_id=98" -H "Origin: You got me!"
