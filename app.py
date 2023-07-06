from flask import Flask, render_template, request
from forex_python.converter import CurrencyRates, CurrencyCodes

app = Flask(__name__)

# A dictiionary list of countries and their three-letter currency codes
countries = {
    "United States": "USD",
    "Australia": "AUD",
    "Brazil": "BRL",
    "Canada": "CAD",
    "China": "CNY",
    "Eurozone": "EUR",
    "India": "INR",
    "Japan": "JPY",
    "Mexico": "MXN",
    "New Zealand": "NZD",
    "Russia": "RUB",
    "Saudi Arabia": "SAR",
    "South Africa": "ZAR",
    "South Korea": "KRW",
    "Switzerland": "CHF",
    "United Kingdom": "GBP",
}


@app.route("/", methods=["GET", "POST"])
def currency_converter():
    if request.method == "POST":
        base_currency = request.form["base_currency"]
        target_currency = request.form["target_currency"]
        amount = request.form["amount"]

        c = CurrencyRates()
        cc = CurrencyCodes()

        try:
            converted_amount = c.convert(base_currency, target_currency, float(amount))
            symbol = cc.get_symbol(target_currency)
            converted_amount_rounded = round(converted_amount, 2)
            result = f"{symbol} {converted_amount: .2f}"
            return render_template("result.html", result=result, countries=countries)
        except (ValueError, KeyError):
            error_message = "Invalid currency code or amount. Please try again."
            return render_template("error.html", message=error_message)
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return render_template("error.html", message=error_message)

    return render_template("index.html", countries=countries)


if __name__ == "__main__":
    app.run()
