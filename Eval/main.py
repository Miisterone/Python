# ==============================================================================
# IMPORTS
# ==============================================================================
import crypto
import leet_speak
import utilities


# ==============================================================================
# GLOBAL VARIABLE
# ==============================================================================*

exit = False
check = False



# ==============================================================================
# SUB FUNCTIONS
# ==============================================================================

def menu_management():
    """
               This function display all messages,questions and patterns.

               :return: None
    """

    global action
    global exit
    global check

    while exit == False:
        print("/==")
        print("| All the following actions are available:")
        print("| Q - Quit the application.")
        print("| A - Encrypt message to leet speak.")
        print("| B - Decrypt form leet speak message.")
        print("| C - Encrypt basic message.")
        print("| D - Decrypt basic message.")

        while check == False:
            action = input("| Select your action:")
            if action in ["Q", "q"]:
                print("")
                print("/==")
                stop = input("| Do you really wish quit the application (Y/N) ?")
                while True:
                    if stop in ["Y", "y"]:
                        print("\==")
                        quit()
                    if stop in ["N", "n"]:
                        print("\==")
                        print("")
                        menu_management()
                    else:
                        print("| Please enter a correct answer!")

            if action in ["A", "a"]:
                print("")
                print("/===")
                leet_speak.encrypt_message()
                print("\\===")
                print("")
                menu_management()

            if action in ["B", "b"]:
                print("")
                print("/===")
                leet_speak.decrypt_message()
                print("\\===")
                print("")
                menu_management()

            if action in ["C", "c"]:
                print("")
                print("/===")
                crypto.encrypt_message()
                print("\\===")
                print("")
                menu_management()
            if action in ["D", "d"]:
                print("")
                print("/===")
                crypto.decrypt_message()
                print("\\===")
                print("")
                menu_management()
            else:
                print("| Please enter a correct answer!")


# ==============================================================================
# PROCESS
# ==============================================================================

if __name__ == '__main__':

    menu_management()
