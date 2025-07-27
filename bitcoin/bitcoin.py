import requests
import sys
import json

try:
    if len(sys.argv[0:]) == 1:
        sys.exit("Command-line argument is not a number")
    if len(sys.argv[0:]) == 2:
        a = float(sys.argv[1])
        response = dict(requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=45ab99b0227bd77181b1a78289f12e80b5e87e0f780938967281c99103deec7b").json())
        data = response["data"]
        unit_price = float(data['priceUsd'])
        price = unit_price*a
        print(f"${price:,.4f}")
except ValueError or requests.RequestException:
    sys.exit("Command-line argument is not a number")
