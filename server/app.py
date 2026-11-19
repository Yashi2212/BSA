import os
from flask import Flask, render_template
from flask import jsonify
from flask import request
import stripe

app = Flask(__name__)

pkey = os.environ.get('STRIPE_PUBLISHABLE_KEY', '')
skey = os.environ.get('STRIPE_SECRET_KEY', '')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/checkout', methods=['GET','POST'])
def checkout():
    if request.method == 'POST':
        stripe.api_key = skey
        customer = stripe.Customer.create(email=request.form['email'])
        ephemeralKey = stripe.EphemeralKey.create(
            customer=customer['id'],
            stripe_version='2022-11-15',
        )
        paymentIntent = stripe.PaymentIntent.create(
            amount=int(float(request.form['amount'])),
            currency='inr',
            customer=customer['id'],
            automatic_payment_methods={
            'enabled': True,
            },
        )
        print(f"Log: {request.form.values()}")
        return jsonify(paymentIntent=paymentIntent.client_secret,
                        ephemeralKey=ephemeralKey.secret,
                        customer=customer.id,
                        publishableKey=pkey)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
 