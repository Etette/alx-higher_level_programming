#!/bin/bash
# Take a URL and display the HTTP methods used
curl -sI "$1" | grep Allow | cut -d " " -f2-
