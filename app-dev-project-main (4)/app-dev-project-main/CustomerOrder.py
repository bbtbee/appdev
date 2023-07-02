import re
import shelve
#previous_id = 0
#for key in order_dict:
# if key.id > previous id:
# previous_id = key.id
# count_id = previous_id
class Customer():
    count_id = 0
    def __init__(self, user_name, name_of_item, price, no_of_items, total_price, email,collection, address):
        Customer.count_id += 1
        self.__order_id = Customer.count_id
        self.__user_name=user_name
        self.__name_of_item = name_of_item
        self.__price = price
        self.__no_of_items=no_of_items
        self.__total_price=total_price
        self.__email = email
        self.__collection = collection
        self.__address = address



    def get_email(self):
        return self.__email


    def get_collection(self):
        return self.__collection
    

    def get_address(self):
        return self.__address

    def set_order_id(self, order_id):
        self.__order_id = order_id


    def set_email(self, email):
        self.__email = email


    def set_collection(self, collection):
        self.__collection = collection

    def set_address(self, address):
        self.__address = address

    def get_order_id(self):
        return self.__order_id

    def get_user_name(self):
        return self.__user_name

    def get_name_of_item(self):
        return self.__name_of_item

    def get_price(self):
        return self.__price

    def get_no_of_items(self):
        return self.__no_of_items

    def get_total_price(self):
        return self.__total_price

    def set_user_name(self, user_name):
        self.__user_name = user_name

    def set_name_of_item(self, name_of_item):
        self.__name_of_item = name_of_item

    def set_price(self, price):
        self.__price = price

    def set_no_of_items(self, no_of_items):
        self.__no_of_items = no_of_items

    def set_total_price(self, total_price):
        self.__total_price=total_price
