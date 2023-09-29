#!/bin/bash
# script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond msg display
curl -s -L -XPUT -H "You got me!" -d "user_id=98" 0.0.0.0:5000/catch_me 
