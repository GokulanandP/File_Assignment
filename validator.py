import re, datetime


def validator(**request):

    if request['CreditCardNumber'] and creditcardvalidator(request['CreditCardNumber']):

        if request['CardHolder'] and cardholdervalidator(request['CardHolder']):

            if request['ExpirationDate'] and expirationdatevalidator(request['ExpirationDate']) :

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
            else:
                return False
        else:
            return False
    else:
        return False


# input for credit card need to be 16 digit number without any special character separating it
def creditcardvalidator(cardnumber):
    if re.fullmatch('([0-9]{16})',cardnumber) and type(cardnumber) == str:
        return True
    else:
        return False


def cardholdervalidator(username):
    if re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?',username) and type(username) == str:
        return True
    else:
        return False


def expirationdatevalidator(expirydate):
    try:
        expirydate = datetime.datetime.strptime(expirydate,'%m/%y').date()
    except:
        return False
    today = datetime.datetime.now().strftime("%m/%y")
    today = datetime.datetime.strptime(today,"%m/%y").date()
    if expirydate > today:
        return True
    else:
        return False


def amountvalidator(amount):
    if re.fullmatch('([0-9]+)',amount) and type(amount) == str:
        return True
    else:
        return False