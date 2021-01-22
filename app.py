from flask import request
from flask_api import status,FlaskAPI
from card_details import CardDetails
from payment_methods import PaymentGateway
from validator import validator
app = FlaskAPI(__name__)

data = []

@app.route('/payment',methods=['POST'])
def ProcessPayment():
    if request.method == 'POST':
        if request.form is None:
            return 'The request data missing', status.HTTP_400_BAD_REQUEST

        if validator(**request.form):
            card_details = CardDetails()
            card_details.get_card_details(request.form)
            payment_process = PaymentGateway(request.form['Amount'],card_details)
            payment_successfull = payment_process.make_payment()
            if payment_successfull:
                return 'Successful', status.HTTP_200_OK,
            else:
                return 'Payment failed', status.HTTP_400_BAD_REQUEST
        else:
            return 'The request invalid', status.HTTP_400_BAD_REQUEST


if __name__ == '__main__':
    app.run(debug=True)





