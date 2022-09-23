#!/bin/bash
# send a delete request to a URL passed as argv[0] and display the body of the response
curl -s "$1" -X DELETE
