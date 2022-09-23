#!/bin/bash
# send a JSON POST request to a URL and display body of response
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
