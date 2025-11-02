

def convert_currency(from_currency, to_currency, amount):
    url = f"https://api.exchangerate.host/convert"
    params = {
        "from": from_currency,
        "to": to_currency,
        "amount": amount
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        converted = data['result']
        print(f"💱 {amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}")
    else:
        print("Error fetching exchange rates.")

