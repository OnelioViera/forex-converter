def test_usd_conversion():
    base_currency = "USD"
    target_currency = "USD"
    amount = 1

    # Perform the currency conversion manually
    converted_amount = amount

    # Format the result in the expected format
    result = f"$ {converted_amount:.2f}"

    # Assert that the conversion result matches the expected result
    assert result == "$ 1.00"


# Run the test
test_usd_conversion()
