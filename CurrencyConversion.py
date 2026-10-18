import requests


def convert_SEK_to_USD_latest(amount_sek, api_key="3d0c0c18a03ae9d790435274ced4d8ad"):
    base_url = "https://data.fixer.io/api/latest"
    params = {
        "access_key": api_key,
        "symbols": "SEK,USD"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    # Basic error handling, check if the API call succeeded
    if not data.get("success", False):
        raise ValueError(f"API error: {data.get('error')}")

    rates = data.get("rates", {})
    if "USD" not in rates or "SEK" not in rates:
        raise ValueError("Missing USD/SEK in rates data")

    # Free plan only uses EUR as base, so SEK->USD = (EUR->USD) / (EUR->SEK)
    sek_to_usd_rate = rates["USD"] / rates["SEK"]
    amount_usd = amount_sek * sek_to_usd_rate

    rate_date = data.get("date", "latest")
    print(f"Using latest rate from {rate_date}: 1 SEK ~= {sek_to_usd_rate:.4f} USD")
    print(f"{amount_sek:,} SEK ~= {amount_usd:,.2f} USD")

    return amount_usd


if __name__ == "__main__":
    print("Script started")

    test_amount = 100000
    usd = convert_SEK_to_USD_latest(test_amount,
                                    api_key="3d0c0c18a03ae9d790435274ced4d8ad")
    print("Test conversion result:", usd)