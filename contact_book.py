class ContactInformation(object):

    def __init__(self,first_name,last_name,birthday,email):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__birthday = birthday
        self.__email = email
        first_name = input("")

    def add_first_name(self):
        self.__first_name = "Joris"
        print(self.__first_name)

class ContactBook(object):
    pass



class ControllerBook(object):
    pass




if __name__ == '__main__':
    ContactInformation.add_first_name()