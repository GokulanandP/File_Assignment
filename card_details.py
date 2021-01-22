class CardDetails:
    def __init__(self):
        self.CreditCardNumber = None
        self.CardHolder = None
        self.ExpirationDate = None
        self.SecurityCode = None
        self.Amount = None

    def get_card_details(self,kwargs):
        self.CreditCardNumber = kwargs.get('CreditCardNumber', None)
        self.Amount = kwargs.get('Amount', None)
        self.CardHolder = kwargs.get('CardHolder', None)
        self.SecurityCode = kwargs.get('SecurityCode', None)
        self.ExpirationDate = kwargs.get('ExpirationDate', None)
        return True