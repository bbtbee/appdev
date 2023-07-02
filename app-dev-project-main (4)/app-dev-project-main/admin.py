class Admin:


    # initializer method
    def __init__(self, first_name, last_name, email, phone, password, remarks):
        self.__user_id = email
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone = phone
        self.__password = password
        self.__remarks = remarks

    # accessor methods
    def get_user_id(self):
        return self.__user_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def get_password(self):
        return self.__password

    def get_remarks(self):
        return self.__remarks

    # mutator methods
    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_email(self, email):
        self.__email = email

    def set_phone(self, phone):
        self.__phone = phone

    def set_password(self, password):
        self.__password = password

    def set_remarks(self, remarks):
        self.__remarks = remarks



