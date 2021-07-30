
class Facility(object):
    """describes a single facility"""
    def __init__(self, bank_id, facility_id, interest_rate, amount):
        self.__bank_id = int(bank_id)
        self.__facility_id = int(facility_id)
        self.__interest_rate = float(interest_rate)
        self.__amount = float(amount)
        self.__max_default_likelihood = 0.0
        self.__banned_states = []
        self.__loans = []
        self.__yields = 0.0

    @property
    def max_default_likelihood(self):
        return self.__max_default_likelihood

    @max_default_likelihood.setter
    def max_default_likelihood(self, value):
        if not value:
            return
        self.__max_default_likelihood = float(value)

    @property
    def banned_states(self):
        return self.__banned_states

    @banned_states.setter
    def banned_states(self, value):
        self.__banned_states = value

    @property
    def id(self):
        return self.__facility_id

    @id.setter
    def id(self, value):
        self.__facility_id = value

    @property
    def loans(self):
        return self.__loans

    @loans.setter
    def loans(self, value):
        self.__loans = value

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = float(value)

    @property
    def interest_rate(self):
        return self.__interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        self.__interest_rate = float(value)

    @property
    def yields(self):
        return self.__yields

    @yields.setter
    def yields(self, value):
        self.__yields = float(value)

    

