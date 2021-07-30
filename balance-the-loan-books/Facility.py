class Facility(object):
    """describes a single facility"""
    def __init__(self, bank_id: int, facility_id: int, interest_rate: float, amount: int):
        self.__bank_id = bank_id;
        self.__facility_id = facility_id;
        self.__interest_rate = interest_rate
        self.__amount = amount
        self.__max_default_likelihood = None
        self.__banned_states = []
        self.__loans = []

    @property
    def max_default_likelihood(self):
        return __max_default_likelihood

    @property
    def banned_states(self):
        self.__banned_states

    @property
    def loans(self):
        self.__loans

    @property
    def amount(self):
        self.__amount

    

