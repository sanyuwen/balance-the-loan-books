from Facility import Facility

class Loan(object):
    """a loan"""
    def __init__(self, id, amount, interest_rate, default_likelihood, state):
        self.__id = int(id)
        self.__amount = int(amount)
        self.__interest_rate = float(interest_rate)
        self.__default_likelihood = float(default_likelihood)
        self.__state = state

    def expected_yield(self, facility: Facility):
        return (1 - self.__default_likelihood) * self.__interest_rate * self.__amount - self.__default_likelihood * self.__amount - facility.interest_rate * self.__amount

    @property
    def default_likelihood(self):
        return self.__default_likelihood

    @property
    def amount(self):
        return self.__amount

    @property
    def id(self):
        return self.__id

    @property
    def state(self):
        return self.__state


