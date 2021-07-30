import csv
import os

from Facility import Facility
from Loan import Loan
from Bank import Bank

class DataStore(object):
    """data access layer"""
    def __init__(self, path: str):
        self.__path = path
        self.__all_facilities = dict()
        self.__banks = dict()
        self.__assignments = dict() # loan id => facility id

    @property
    def all_facilities(self):
        return self.__all_facilities

    @property
    def assignments(self):
        return self.__assignments

    def get_full_path(self, file_name: str) -> str:
        return os.path.join(self.__path, file_name)

    def read_banks(self, file_name = "banks.csv"):
        with open(self.get_full_path(file_name), 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for id, name in csvreader:
                self.__banks[id] = Bank(id, name)

    def read_facilities(self, file_name = "facilities.csv"):
        with open(self.get_full_path(file_name), 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for amount, interest_rate, id, bank_id in csvreader:
                new_facility = Facility(bank_id, id, interest_rate, amount)
                self.__all_facilities[id] = new_facility
                self.__banks[bank_id].facilities.append(new_facility)

    def read_covenants(self, file_name = "covenants.csv"):
        with open(self.get_full_path(file_name), 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for facility_id, max_default_likelihood, bank_id, banned_state in csvreader:
                if not facility_id:
                    # applied to all facilities in the bank
                    bank = self.__banks[bank_id]
                    for i in range(len(bank.facilities)):
                        facility = bank[i]
                        facility.max_default_likelihood = max_default_likelihood
                        facility.banned_state.append(banned_state)
                # applied to facility with this id
                if facility_id in self.__all_facilities:
                    facility = self.__all_facilities[facility_id]
                    facility.max_default_likelihood = max_default_likelihood
                    facility.banned_states.append(banned_state)

    def export_assignments(self, file_name = "assignments.csv"):
        full_path = self.get_full_path(file_name)
        with open(full_path, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["loan_id", "facility_id"])
            for loan_id, facility_id in self.__assignments.items():
                csvwriter.writerows([loan_id, facility_id])
        return full_path

    
    def export_yields(self, file_name = "yields.csv"):
        full_path = self.get_full_path(file_name)
        with open(full_path, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["facility_id", "expected_yield"])
            for id, facility in self.__all_facilities.items():
                csvwriter.writerows([id, facility.yields])
        return full_path
                    
  


