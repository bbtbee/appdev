# User class
class UserOrder:
    count_id = 0

    # initializer method
    def __init__(self, name_of_item, price, no_of_items, total_price,collection,address):
        UserOrder.count_id += 1
        self.__user_order_id = UserOrder.count_id
        self.__name_of_item = name_of_item
        self.__price = price
        self.__no_of_items=no_of_items
        self.__collection = collection
        self.__address = address
        self.__total_price=total_price

    # accessor methods
    def get_user_order_id(self):
        return self.__user_order_id

    def get_collection(self):
        return self.__collection

    def get_address(self):
        return self.__address
    

    def set_collection(self, collection):
        self.__collection = collection

    def set_address(self, address):
        self.__address = address

    def get_name_of_item(self):
        return self.__name_of_item

    def get_price(self):
        return self.__price

    def get_no_of_items(self):
        return self.__no_of_items

    def get_total_price(self):
        return self.__total_price

    def set_name_of_item(self, name_of_item):
        self.__name_of_item = name_of_item

    def set_price(self, price):
        self.__price = price

    def set_no_of_items(self, no_of_items):
        self.__no_of_items = no_of_items

    def set_total_price(self, total_price):
        self.__total_price=total_price

    # mutator methods
    def set_user_order_id(self, user_order_id):
        self.__user_order_id = user_order_id

