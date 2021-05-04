import time


class Home(object):

    def __init__(self, home_name):
        print(
            " + Creation of new house named '{0}'.".format(home_name)
        )
        self.__name = home_name
    def __del__(self):
        print(
            " + Destruction of home named '{0}'.".format(self.__name)
        )

if __name__ == '__main__':
    print("Home creation")
    my_house = Home("Home 1")
    print("Deletion of home")
    del my_house

    print("-- End of program --\n\n")
    time.sleep(10)