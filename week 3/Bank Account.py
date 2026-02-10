class BankAccount():
    '''A class representing bank accounts'''
    def __init__(self, account_number = '00-00-00', account_value = 120000.0, interest_rate = 0.05):
        self.__account_number = account_number
        self.__account_value = account_value
        self.__interest_rate = interest_rate

    def get_account_value(self):
        return self.__account_value

    def set_account_value(self, account_value):
        self.__account_value = account_value
