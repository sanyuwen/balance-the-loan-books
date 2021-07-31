import unittest
import csv
from DataStore import DataStore
from Dispatcher import Dispatcher
from Loan import Loan

class Test_test_balance_the_loan_books(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test_test_balance_the_loan_books, self).__init__(*args, **kwargs)
        self.__data_store = DataStore("D:\Download\large")
        self.__data_store.read_banks()
        self.__data_store.read_facilities()
        self.__data_store.read_covenants()
        self.__loans = dict()
        self.__dispatcher = Dispatcher(self.__data_store)

    def read_loans(self, file_name = "loans.csv"):
        with open(self.__data_store.get_full_path(file_name), 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for interest_rate, amount, id, default_likelihood, state in csvreader:
                self.__loans[id] = Loan(id, amount, interest_rate, default_likelihood, state)

    def test_assign_loan_correct(self):
        # load id => facility id
        # when test with small datasets
        #desired_results = {"1": 1, "2": 2, "3": 1}
        self.read_loans()

        for id, loan in self.__loans.items():
            result = self.__dispatcher.dispatch(loan)
            #print(f"{id} => {result}")
            #self.assertEqual(result, desired_results[id])

        #for id, facility in self.__data_store.all_facilities.items():
        #    print(f"{id} yields: {facility.yields}")
        self.__data_store.export_assignments()
        self.__data_store.export_yields()
        

if __name__ == '__main__':
    unittest.main()
