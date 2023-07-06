# from flask import Flask, render_template, request
# from forex_python.converter import CurrencyRates, CurrencyCodes

# app = Flask(__name__)

# # A dictiionary list of countries and their three-letter currency codes
# countries = {
#     "USD": "United States",
#     "AUD": "Australia",
#     "BRL": "Brazil",
#     "CAD": "Canada",
#     "CNY": "China",
#     "EUR": "Eurozone",
#     "INR": "India",
#     "JPY": "Japan",
#     "MXN": "Mexico",
#     "NZD": "New Zealand",
#     "RUB": "Russia",
#     "SAR": "Saudi Arabia",
#     "ZAR": "South Africa",
#     "KRW": "South Korea",
#     "CHF": "Switzerland",
#     "GBP": "United Kingdom",
# }


# @app.route("/", methods=["GET", "POST"])
# def currency_converter():
#     if request.method == "POST":
#         base_currency = request.form["base_currency"]
#         target_currency = request.form["target_currency"]
#         amount = request.form["amount"]

#         if base_currency == target_currency:
#             error_message = "Please select different currencies for conversion."
#             return render_template("error.html", message=error_message)

#         c = CurrencyRates()
#         cc = CurrencyCodes()

#         try:
#             converted_amount = c.convert(base_currency, target_currency, float(amount))
#             symbol = cc.get_symbol(target_currency)
#             converted_amount_rounded = round(converted_amount, 2)
#             result = f"{symbol} {converted_amount: .2f}"
#             return render_template("result.html", result=result, countries=countries)
#         except (ValueError, KeyError):
#             error_message = "Invalid currency code or amount. Please try again."
#             return render_template("error.html", message=error_message)
#         except Exception as e:
#             error_message = f"An error occurred: {str(e)}"
#             return render_template("error.html", message=error_message)

#     return render_template("index.html", countries=countries)


# if __name__ == "__main__":
#     app.run()


from flask import Flask, render_template, request
from forex_python.converter import CurrencyRates, CurrencyCodes

app = Flask(__name__)

countries = {
    "USD": "United States",
    "EUR": "Eurozone",
    "GBP": "United Kingdom",
    "CAD": "Canada",
    "AUD": "Australia",
    "JPY": "Japan",
    "CHF": "Switzerland",
    "NZD": "New Zealand",
    "ZAR": "South Africa",
    "INR": "India",
    "CNY": "China",
    "BRL": "Brazil",
    "MXN": "Mexico",
    "RUB": "Russia",
    "KRW": "South Korea",
    "SAR": "Saudi Arabia",
}


@app.route("/", methods=["GET", "POST"])
def currency_converter():
    if request.method == "POST":
        base_currency = request.form["base_currency"]
        target_currency = request.form["target_currency"]
        amount = request.form["amount"]

        if base_currency == target_currency:
            error_message = "Please select different currencies for conversion."
            return render_template("error.html", message=error_message)

        c = CurrencyRates()
        cc = CurrencyCodes()

        try:
            converted_amount = c.convert(base_currency, target_currency, float(amount))
            symbol = cc.get_symbol(target_currency)
            result = f"{symbol} {converted_amount:.2f}"
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
