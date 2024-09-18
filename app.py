from flask import Flask, render_template, request

app = Flask(__name__)

# Prices
OneVadaiPrice = 30.0
OneSodaPrice = 20.0
OneSandwichPrice = 100.0
OneTeaPrice = 10.0
OneCoffeePrice = 15.0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buy', methods=['GET', 'POST'])
def buy():
    if request.method == 'POST':
        # Get quantities from form
        vadai_qty = int(request.form.get('vadai', 0))
        soda_qty = int(request.form.get('soda', 0))
        sandwich_qty = int(request.form.get('sandwich', 0))
        tea_qty = int(request.form.get('tea', 0))
        coffee_qty = int(request.form.get('coffee', 0))

        # Calculate cost for each item
        vadai_cost = vadai_qty * OneVadaiPrice
        soda_cost = soda_qty * OneSodaPrice
        sandwich_cost = sandwich_qty * OneSandwichPrice
        tea_cost = tea_qty * OneTeaPrice
        coffee_cost = coffee_qty * OneCoffeePrice

        # Calculate total price
        total_price = vadai_cost + soda_cost + sandwich_cost + tea_cost + coffee_cost

        # Calculate balance if user has paid
        given_amount = float(request.form.get('given_amount', 0))
        balance = given_amount - total_price if given_amount >= total_price else None

        return render_template('receipt.html', total_price=total_price, balance=balance)
    
    return render_template('buy.html')

if __name__ == '__main__':
    app.run(debug=True)
