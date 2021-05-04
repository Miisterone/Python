# ==============================================================================
# IMPORTS
# ==============================================================================
import datetime
import json

from Jeu import user_management,finder_management,randomize_management

# ==============================================================================
# GLOBAL VARIABLE
# ==============================================================================


message = ""
user_in_play = None
value_out = 0
formatting = ""
game_number = 0
check = False
check2 = False
check3 = False

a = []


# ==============================================================================
# SUB FUNCTIONS
# ==============================================================================

def create_new_user():
    """
        The function create users.
        :return: none
    """
    global user_in_play

    print("/==")
    user_management.load_statistics()
    print("\\==")

    if len(user_management.all_users_information["users"]) == user_management.all_users_information["max_user"]:
        print("")
        print("/==")
        print("| Maximum number of users reached")
        print("\\==")

    while len(user_management.all_users_information["users"]) < 1:
        print("")
        print("/==")
        print("| There is no previous user. Create a new one...")
        print("\\==")

        print("")
        print("/==")
        user_id = user_management.add_new_user()
        print("| New user '{}' have been created".format(user_management.get_user_name(user_id)))
        print("\\==")
        user_management.save_statistics()

        print("")
        print("/==")
        print("| Good luck user '{}'".format(user_management.get_user_name(user_id)))
        print("\\==")
        user_in_play = user_management.get_user_name(user_id)
    return user_in_play


def user_selection():
    """
            The function create users.
            :return: none
    """
    global check
    global check2

    create_new_user()

    print("")
    print("/==")
    print("| List of existing user: ")
    for user_key in user_management.get_list_of_users():
        print("|   {0} | '{1}'".format(user_key[0], user_key[1]))
        a.append(user_key[0])
    print("\\==")

    print("")
    print("/==")
    if len(user_management.all_users_information["users"]) <= user_management.all_users_information["max_user"]:
        while check == False:
            select_user = input("| Do you wish to create or use existing user (C/U) ?")
            if select_user in ["C", "c"]:
                    check = True
                    print("")
                    print("/==")
                    user_id = user_management.add_new_user()
                    print("| New user '{}' have been created".format(user_management.get_user_name(user_id)))
                    print("\\==")
                    user_management.save_statistics()
                    print("")
                    print("/==")
                    print("| Good luck user '{}'".format(user_management.get_user_name(user_id)))
                    print("\\==")
            elif select_user in ["U", "u"]:
                check = True
                print("\\==")
                print("")
                print("/==")
                while check2 == False:
                    select_id = input("| Select an existing user by ID from previous list: ?")
                    if select_id in a:
                        check2 = True
                        print("\\==")
                        print("")
                        print("/==")
                        print("| Good luck user '{}'".format(user_management.get_user_name(select_id)))
                    else:
                        print("| Please enter a correct answer!")
                print("\\==")
            else:
                print("| Please enter a correct answer!")

def range_change_proposal():
    global check3

    print("")
    print("/==")
    while check3 == False:
        check3 = True
        print("| Range available for each game:")
        print("| 1 - Original [0-1000]")
        print("| 2 - Default [100-200]")
        print("| 3 - Yours")
        range = input("| Select the range for your next game:")
        if range in ["1"]:
            print("")
            finder_management.start_the_finder()
            check_end_of_the_game()
        if range in ["2"]:
            finder_management.user_lower_limit = 100
            finder_management.user_upper_limit = 200
            finder_management.game = 4
            print("")
            finder_management.start_the_finder()
            check_end_of_the_game()
        if range in ["3"]:
            user_lower_limit = input("| Give me the new lower limit (Default if empty):")
            user_lower_limit = int(user_lower_limit)
            finder_management.user_lower_limit = user_lower_limit

            user_upper_limit = input("| Give me the new upper limit (Default if empty):")
            user_upper_limit = int(user_upper_limit)
            finder_management.user_upper_limit = user_upper_limit

            finder_management.game = 4
            print("")
            finder_management.start_the_finder()
            check_end_of_the_game()
        else:
            print("| Please enter a correct answer!")
    print("\\==")


def check_end_of_the_game():
    print("")
    print("/==")
    print("| Users statistics saved!")
    print("\\==")
    user_management.save_statistics()
    print("")
    print("/==")
    end = input("| Do you wish to relaunch a game (Y/N)?")
    print("\\==")
    print("")
    if end in ["Y", "y"]:
        finder_management.game = 4
        print("\\==")
        print("")
        finder_management.start_the_finder()
    if end in ["N", "n"]:
        display_user_statistics()
        exit()
    else:
        print("| Please enter a correct answer!")


def display_user_statistics():
    print("/==")
    for user_key in  user_management.get_list_of_users():
        s = user_management.all_users_information["users"][user_key[0]]["statistics"]
        print("|        Date|   Range min |     Range max |     Number of try")
        print("| {}".format(json.dumps(s)))
    print("\\==")


# ==============================================================================
# PROCESS
# ==============================================================================

# Main function
if __name__ == '__main__':
    user_selection()
    range_change_proposal()


