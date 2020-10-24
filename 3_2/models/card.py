class Card():
    __value: str
    __suit: str

    def __init__(self, value, suit):
        self.__value = value
        self.__suit = suit

    def get_name(self):
        return self.__suit + self.__value

    def get_suit(self):
        return self.__suit

    def set_suit(self, suit):
        self.__suit = suit

    def get_value(self):
        return self.__value