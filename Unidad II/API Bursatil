import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&symbol=IBM&apikey=GRRKF4OAUQ1AWSU0'

while True:
    id = int(input("Ingresa el id: "))
    if id == 'salir' or id == 's':
        break
    json_data = requests.get(url).json()
    print(f"symbol: {json_data["data"][0]["symbol"]}")
    print(f"type: {json_data["data"][0]["type"]}")
    print(f"contractID: {json_data["data"][0]["contractID"]}")
