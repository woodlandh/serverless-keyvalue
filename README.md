# serverless-blink1

[![serverless](http://public.serverless.com/badges/v3.svg)](http://www.serverless.com)

A serverless endpoint to push and fetch alphanumeric keys and values.

This project uses:

* python2.7 (because Lambda)
* [Serverless Framework](https://github.com/serverless/serverless)
* [boto3](https://boto3.readthedocs.io/en/latest/)
* [pyresttest](https://github.com/svanoort/pyresttest) for testing


## Install

Make sure you have the [Serverless Framework](http://www.serverless.com) installed and you're using Node.js v4.0+. 
```
npm install serverless -g
```

Deploy your functions and endpoints from the project root directory:
```
serverless deploy
```

Output should look something like this:
```
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Creating Stack...
Serverless: Checking Stack create progress...
Serverless: Stack create finished...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service .zip file to S3 (8.05 MB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
Serverless: Stack update finished...
Service Information
service: keyvalue
stage: v001
region: us-west-2
stack: keyvalue-v001
api keys:
  None
endpoints:
  POST - https://svzi5fr499.execute-api.us-west-2.amazonaws.com/v001/keys
  GET - https://svzi5fr499.execute-api.us-west-2.amazonaws.com/v001/keys
  GET - https://svzi5fr499.execute-api.us-west-2.amazonaws.com/v001/key/{keyname}
  PUT - https://svzi5fr499.execute-api.us-west-2.amazonaws.com/v001/key/{keyname}
  DELETE - https://svzi5fr499.execute-api.us-west-2.amazonaws.com/v001/key/{keyname}
functions:
  create: keyvalue-v001-create
  list: keyvalue-v001-list
  get: keyvalue-v001-get
  update: keyvalue-v001-update
  delete: keyvalue-v001-delete
```

Copy your base URL to your clipboard, you'll need it. Exclude the trailing forward-slash.
```
https://XXXXXXXXXX.execute-api.us-west-2.amazonaws.com
```

## Usage

You can interact with the API using curl. I've created `run_example.sh` with simple CRUD operations. Use it like so:
```
./run_example.sh https://XXXXXXXXXX.execute-api.us-west-2.amazonaws.com
```

Expected output something like:
```
{"text": "baseball, hockey, football", "keyname": "sports", "createdAt": 1506970587350, "updatedAt": 1506970587350}
{"text": "baseball, hockey, football", "keyname": "sports", "createdAt": 1506970587350, "updatedAt": 1506970587350}
{"text": "baseball, hockey, soccer", "keyname": "sports", "createdAt": 1506970587350, "updatedAt": 1506970588924}
{"text": "baseball, hockey, soccer", "keyname": "sports", "createdAt": 1506970587350, "updatedAt": 1506970588924}
[]
```

##Testing

#### pyresttest

This requires pyrresttest. You can install it with pip.

Usage:
```
./run_test.sh https://XXXXXXXXXX.execute-api.us-west-2.amazonaws.com
```

Expected output, condensed:
```
blahblahblah
...
Test Group default SUCCEEDED: : 8/8 Tests Passed!
```

