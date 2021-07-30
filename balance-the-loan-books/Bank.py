class Bank(object):
    """describes a banking partner"""
    def __init__(self, bank_id, bank_name):
        self.__bank_id = int(bank_id)
        self.__bank_name = bank_name
        self.__facilities = []

    @property
    def facilities(self):
        return self.__facilities



