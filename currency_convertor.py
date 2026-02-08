import requests


API_URL = "https://api.exchangerate-api.com/v4/latest/"


def fetch_exchange_rates(base_currency: str) -> dict:
    """
    Fetch live exchange rates for a given base currency.
    """
    response = requests.get(API_URL + base_currency)
    response.raise_for_status()
    return response.json()


def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    """
    Convert amount from one currency to another using live rates.
    """
    data = fetch_exchange_rates(from_currency)
    rate = data["rates"].get(to_currency)

    if rate is None:
        raise ValueError("Invalid target currency")

    return amount * rate


def main():
    print("💱 Currency Converter")

    amount = float(input("Enter amount: "))
    from_currency = input("From currency (e.g. USD): ").upper()
    to_currency = input("To currency (e.g. PKR): ").upper()

    try:
        converted_amount = convert_currency(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
