#!/bin/bash

curl -X POST $1/v001/keys --data '{ "keyname": "sports", "text": "baseball, hockey, football" }'
curl $1/v001/key/sports
curl -X PUT $1/v001/key/sports --data '{ "text": "baseball, hockey, soccer" }'
curl $1/v001/key/sports
curl -X DELETE $1/v001/key/sports
curl $1/v001/keys
