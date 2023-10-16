import requests

url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json"
response = requests.get(url)
data = response.json()

result = {elem["cc"]: elem["rate"] for elem in data}

while True:
    amount = float(input("Enter the amount: "))
    currency = input("Enter the currency code for conversation (USD, EUR, PLN): ").upper()

    if currency not in result:
        print("Currency not found")
    else:
        convert = amount * result[currency]
        print(f"{amount} {currency} = {convert:.2f} UAH")