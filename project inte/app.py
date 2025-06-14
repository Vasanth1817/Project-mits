from flask import Flask, render_template, request

app = Flask(__name__)

# Static currency rates for demo (1 unit of FROM = x units of TO)
mock_rates = {
    ('USD', 'INR'): 83.5,
    ('INR', 'USD'): 0.012,
    ('USD', 'EUR'): 0.93,
    ('EUR', 'USD'): 1.07,
    ('EUR', 'INR'): 89.0,
    ('INR', 'EUR'): 0.011
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None

    if request.method == 'POST':
        from_currency = request.form.get('from_currency', '').upper()
        to_currency = request.form.get('to_currency', '').upper()
        amount = request.form.get('amount', '')

        try:
            amount = float(amount)
            key = (from_currency, to_currency)
            if key in mock_rates:
                result = round(amount * mock_rates[key], 2)
            else:
                error = f"No conversion rate for {from_currency} to {to_currency}."
        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
