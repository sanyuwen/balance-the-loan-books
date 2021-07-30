class Loan(object):
    """a loan"""
    def __init__(self, id: int, amount: int, interest_rate: float, default_likelihood: float, state: str):
        self.__id = id
        self.__amount = amount
        self.__interest_rate = interest_rate
        self.__default_likelihood = default_likelihood
        self.__state = state

    def expected_yield(self):
        pass


