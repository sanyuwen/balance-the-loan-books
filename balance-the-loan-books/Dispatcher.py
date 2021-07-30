from Facility import Facility
from Loan import Loan
from Bank import Bank
from DataStore import DataStore

class Dispatcher(object):
    """description of class"""
    def __init__(self, data_store: DataStore):
        self.__data_store = data_store

    def dispatch(self, loan: Loan) -> int:
        available_facilities = [facility for facility in self.__data_store.all_facilities.values() if self.qualify(facility, loan)]
        facility = max(available_facilities, key = lambda facility: loan.expected_yield(facility))
        facility.amount -= loan.amount
        facility.loans.append(loan.id)
        facility.yields += loan.expected_yield(facility)

        # store dispatch information
        self.__data_store.assignments[loan.id] = facility.id

        return facility.id


    def qualify(self, facility: Facility, loan: Loan) -> bool:
        return all((
            facility.max_default_likelihood >= loan.default_likelihood,
            loan.state not in facility.banned_states,
            loan.amount <= facility.amount
            ))
