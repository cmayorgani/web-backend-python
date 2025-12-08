#!/usr/bin/env bash
set -euo pipefail

AWS="awslocal"

# Simular una lambda que no hace nada (placeholder)
echo 'exports.handler = async () => ({ statusCode: 200, body: "OK" })' > /tmp/index.js
zip -j /tmp/lambda.zip /tmp/index.js

$AWS lambda create-function --function-name FrontendLambda \
  --runtime nodejs18.x --handler index.handler \
  --zip-file fileb:///tmp/lambda.zip \
  --role arn:aws:iam::000000000000:role/lambda-role || true
