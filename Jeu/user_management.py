# ==============================================================================
# IMPORTS
# ==============================================================================

import json
import os
import datetime
from Jeu import finder_management

# ==============================================================================
# GLOBAL VARIABLE
# ==============================================================================

all_users_information = {}
first_name_question = "| What is the first name of the user:"
last_name_question = "| What is the last name of the user:"
loading_success_message = "| User statistics loaded!"
loading_failed_message = " | No previous statistics to load..."
saving_message = "User statistics saved"
statistic_file = "statistics.dat"

user = 0
c = 0


# ==============================================================================
# SUB FUNCTIONS
# ==============================================================================

def set_new_max_user():
    """
        This function set the max user

        :return: int
    """
    if get_max_user() == 3:
        all_users_information["max_user"] = 3
    while get_max_user() > all_users_information["max_user"]:
        return get_max_user()


def get_max_user():
    global c
    c = c + 1
    return len(all_users_information["users"]) + 1


def add_new_user():
    global all_users_information
    global loading_success_message
    global user

    name_first = input(first_name_question)
    name_last = input(last_name_question)

    user_id = len(all_users_information["users"])
    all_users_information["users"][str(user_id)] = {
        "id_f_name": name_first,
        "id_l_name": name_last,
        "statistics": {}
    }
    user = user + 1
    add_user_try_result(str(user_id))
    return user_id


def get_list_of_users():
    key = []
    user_key = len(all_users_information["users"])
    for user_key in all_users_information["users"]:
        f_name = all_users_information["users"][str(user_key)]["id_f_name"]
        l_name = all_users_information["users"][str(user_key)]["id_l_name"]
        key.append((user_key, f_name + " " + l_name))
    return key


def add_user_try_result(user_id):
    time = datetime.datetime.now().isoformat()
    all_users_information["users"][user_id]["statistics"][time] = {
        "min": finder_management.user_lower_limit,
        "max": finder_management.user_upper_limit,
        "try": finder_management.try_number
    }


def get_user_statistics(user_key):
    s = all_users_information["users"][user_key[0]]["statistics"]
    return json.dumps(s, indent=4)

def get_user_name(user_key):
    user = all_users_information["users"][str(user_key)]
    return user["id_f_name"] + " " + user["id_l_name"]


def load_statistics():
    global all_users_information

    if os.path.isfile("./statistics.dat"):
        with open(statistic_file, 'r') as openfile:
            # Reading from json file
            all_users_information = json.load(openfile)
            print(loading_success_message)
    else:
        print("| No previous statistics to load...")
        all_users_information = {
            "users": {

            },
            "max_user": 2
        }


def save_statistics():
    with open(statistic_file, "w") as write_file:
        # Write dict to json file
        json.dump(all_users_information, write_file)


# ==============================================================================
# PROCESS
# ==============================================================================

# Main function
if __name__ == '__main__':
    print("/==")
    load_statistics()
    print("\\==")

    set_new_max_user()

    while len(all_users_information["users"]) < all_users_information["max_user"]:
        print("")
        print("/==")
        user_id = add_new_user()
        print("| New user '{}' have been created".format(get_user_name(user_id)))
        print("| Default statistics set to '{}'")
        print("\\==")
    save_statistics()

    if len(all_users_information["users"]) == all_users_information["max_user"]:
        print("")
        print("/==")
        print("| => Maximum number opf user have been reached <=")
        print("\\==")

        print("")
        print("/==")
        print("| Previous maximum of users: '{}'".format(len(all_users_information["users"])))
        print("| New maximum of users: '{}'".format(len(all_users_information["users"])))
        if c == 3:
            print("| Last maximum of users: '{}'".format(all_users_information["max_user"]))
        if c == 2:
            c = 3
            print("| Last maximum of users: '{}'".format(c))
        print("\\==")

        print("")
        print("/==")
        for user_key in get_list_of_users():
            print("| Adding statistic for user: '{0}/{1}'".format(user_key[0], user_key[1]))
        print("\\==")

        print("")
        print("/==")
        for user_key in get_list_of_users():
            print("| All statistic for user: '{0}/{1}'".format(user_key[0], user_key[1]))
            print(get_user_statistics(user_key))
        print("\\==")

    if len(all_users_information["users"]) < all_users_information["max_user"]:
        print("")
        print("/==")
        user_id = add_new_user()
        print("| New user '{}' have been created".format(get_user_name(user_id)))
        print("| Default statistics set to '{}'")
        print("\\==")
    save_statistics()