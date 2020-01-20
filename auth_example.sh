#!/usr/bin/sh
# Example of using curl to authorize and make an API request

username="USERNAME"
password="PASSWORD"
mid="MID"
token_url="TOKEN_URL"
api_url="API_URL"

# request access_token and passing credentials
# parse the returned JSON like string and store the access_token in variable
token=$(curl --request POST \
  --url $token_url \
  --data grant_type=password \
  --data username=$username \
  --data password=$password \
  --data "client_id=${mid}" | jq -r '.access_token')

echo "Access token: $token"

# examplary API request authorized with the access_token
all_devices=$(curl \
  -X GET "${api_url}/otdevice/getall?token=${token}" \
  -H  "accept: application/json" \
  -H  "mid: ${mid}")

echo "All Devices:" 
echo "$all_devices"
