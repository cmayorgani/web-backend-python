#!/usr/bin/env bash
set -euo pipefail

AWS="awslocal"

# Crear buckets S3 para frontend y backend (archivos)
$AWS s3 mb s3://frontend-bucket || true
$AWS s3 mb s3://files-bucket || true

# Subir un index.html placeholder (lo sirve el frontend container, pero dejamos recursos)
echo "<html><body>App desplegada via Lambda/API GW simulado</body></html>" > /tmp/index.html
$AWS s3 cp /tmp/index.html s3://frontend-bucket/index.html

# Crear API Gateway simulado
API_ID=$($AWS apigateway create-rest-api --name "SimAPI" --region us-east-1 --query 'id' --output text)
PARENT_ID=$($AWS apigateway get-resources --rest-api-id $API_ID --query 'items[0].id' --output text)

# Crear recursos /auth, /files, /token
for RES in auth files token; do
  RID=$($AWS apigateway create-resource --rest-api-id $API_ID --parent-id $PARENT_ID --path-part $RES --query 'id' --output text)
  # Mock integration pointing to our containers (we’ll document URLs; LocalStack won’t proxy to localhost automatically)
  $AWS apigateway put-method --rest-api-id $API_ID --resource-id $RID --http-method ANY --authorization-type "NONE"
  $AWS apigateway put-integration --rest-api-id $API_ID --resource-id $RID --http-method ANY --type HTTP --integration-http-method ANY \
    --uri "http://host.docker.internal:8001" || true
done

# Para files y token ajustamos las URIs
FILES_RID=$($AWS apigateway get-resources --rest-api-id $API_ID --query "items[?path=='/files'].id" --output text)
$AWS apigateway put-integration --rest-api-id $API_ID --resource-id $FILES_RID --http-method ANY --type HTTP --integration-http-method ANY \
  --uri "http://host.docker.internal:8002" || true

TOKEN_RID=$($AWS apigateway get-resources --rest-api-id $API_ID --query "items[?path=='/token'].id" --output text)
$AWS apigateway put-integration --rest-api-id $API_ID --resource-id $TOKEN_RID --http-method ANY --type HTTP --integration-http-method ANY \
  --uri "http://host.docker.internal:8003" || true

# Crear y desplegar stage
$AWS apigateway create-deployment --rest-api-id $API_ID --stage-name dev
echo "API_ID=$API_ID" > /var/lib/localstack/api_id.env
echo "API Gateway creado: $API_ID"
