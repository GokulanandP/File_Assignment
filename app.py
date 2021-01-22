from flask import request
from flask_api import status,FlaskAPI
import re, datetime
from card_details import CardDetails
from payment_methods import PaymentGateway
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
            payment_process = PaymentGateway(request.form['Amount'] ,card_details)
            payment_sccessfull = payment_process.make_payment()
            if payment_sccessfull:
                return 'Successful', status.HTTP_200_OK,
            else:
                return 'Payment failed', status.HTTP_400_BAD_REQUEST
        else:
            return 'The request invalid', status.HTTP_400_BAD_REQUEST


def validator(**request):

    if request['CreditCardNumber'] and creditcardvalidator(request['CreditCardNumber']):

        if request['CardHolder'] and cardholdervalidator(request['CardHolder']):

            # if request['ExpirationDate'] and expirationdatevalidator(request['ExpirationDate']) :

            if request['Amount'] and amountvalidator(request['Amount']):

                if request['Security']:
                    if re.fullmatch('[0-9]{3}', str(request['Security'])):
                        pass
                    else:
                        return False

                else:
                    pass

                return True

            else:
                return False
        # else:
        #     return 'The request is invalid', status.HTTP_400_BAD_REQUEST
        else:
            return False
    else:
        return False


# input for credit card need to be 16 digit number without any special character separating it
def creditcardvalidator(cardnumber):
    if re.fullmatch('([0-9]{16})',str(cardnumber)):
        return True
    else:
        return False


def cardholdervalidator(username):
    if re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?',str(username)):
        return True
    else:
        return False


def expirationdatevalidator(expirydate):
    expirydate = datetime.datetime.strptime(str(expirydate),"%m/%Y").date()
    today = datetime.datetime.now()
    # if expirydate > datetime.datetime(today.month,today.year,1):


def amountvalidator(amount):
    if re.fullmatch('([0-9]+)',amount):
        return True
    else:
        return False

if __name__ == '__main__':
    app.run(debug=True)





