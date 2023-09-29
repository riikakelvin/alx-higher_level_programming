#!/bin/bash
# scrip taking in a URL and displays all HTTP methods acceptable
curl -sI  "$1" | sed -n '/Allow: /s/Allow: //p'
