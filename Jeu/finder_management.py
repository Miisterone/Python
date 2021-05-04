# ==============================================================================
# IMPORTS
# ==============================================================================

import randomize_management

# ==============================================================================
# GLOBAL VARIABLE
# ==============================================================================

main_question = "| Aim of this game is to find a randomized number as:"
lower_question = "| - Lower or equal to"
upper_question = "| - Upper or equal to"
good_answer = "| Yes. It is! You win!"
try_number = 0
count_display = "| Success in '{0}' attempt"
bad_lower_answer = "| No. It's lower..."
bad_upper_answer = "| No. It's upper..."

n = 0
game = 0
game_number = 0
user_upper_limit = 0
user_lower_limit = 0
SUBS = [
    ("IIIII", "V"),
    ("VV", "X"),
    ("XXXXX", "L"),
    ("LL", "C"),
    ("CCCCC", "D"),
    ("DD", "M"),
    ("IIII", "IV"),
    ("VIV", "IX"),
    ("XXXX", "XL"),
    ("LXL", "XC"),
    ("CCCC", "CD"),
    ("DCD", "CM"),
]


# ==============================================================================
# SUB FUNCTIONS
# ==============================================================================

def start_the_finder():
    """
           This function display the entire game.

           :return: None
    """
    global try_number
    # To get 5 games
    while game < 5:
        display_game()
        print("/=======================================================")
        print("| Game {}".format(to_roman(game_number)))
        print("|=======================================================")
        limits_modify()
        print(main_question)
        print(lower_question, "'{}'".format(randomize_management.internal_lower_limit))
        print(upper_question, "'{}'".format(randomize_management.internal_upper_limit))
        print("|=======================================================")
        check_the_number()
        try_number = 0



def to_roman(n):
    """
              This function convert int into roman number.

              :return: str
       """
    res = "I" * n
    for r in SUBS:
        res = res.replace(*r)
    return res


def to_int(n):
    """
        This function convert roman into int number.
        :return: str
    """
    res = n
    for r in SUBS[::-1]:
        res = res.replace(*r[::-1])
    return len(res)

def ask_the_number_to_user():
    """
        This function ask the question.
        :return: int
    """
    global n
    n = input("| Give me a number:")
    n = int(n)
    return n


def check_the_number():
    """
        The function checks if the user enters the correct number.
        :return: none
    """
    global try_number
    global game
    r = randomize_management.random_number()
    while True:
        ask_the_number_to_user()
        if n == r:
            try_number = try_number + 1
            game = game + 1
            congrats_user()
            break
        if n > r:
            print(bad_lower_answer)
            print("|=======================================================")
            try_number = try_number + 1
        else:
            print(bad_upper_answer)
            print("|=======================================================")
            try_number = try_number + 1


def limits_modify():
    """
        The function changes the limits of the values.
        :return: none
    """
    global user_lower_limit, user_upper_limit
    # Warning game start at 0 so the first game , game = 0
    if game == 1:
        randomize_management.internal_lower_limit = 0
        randomize_management.internal_upper_limit = 1000
    if game == 2:
        # Request the new lower limit
        user_lower_limit = input("| Give me a new lower limit:")
        user_lower_limit = int(user_lower_limit)
        print("|=======================================================")
        # Change the last lower limit by the new
        randomize_management.internal_lower_limit = user_lower_limit
        randomize_management.internal_upper_limit = 1000
    if game == 3:
        # Request the new upper limit
        user_upper_limit = input("| Give me a new upper limit:")
        user_upper_limit = int(user_upper_limit)
        print("|=======================================================")
        # Change the last upper limit by the new
        randomize_management.internal_lower_limit = 0
        randomize_management.internal_upper_limit = user_upper_limit
    if game == 4:
        randomize_management.internal_lower_limit = user_lower_limit
        randomize_management.internal_upper_limit = user_upper_limit


def congrats_user():
    """
        The function congratulates the user.
        :return: none
    """
    print(good_answer)
    print(count_display.format(try_number))
    print("\\=======================================================")
    print("\n")


def display_game():
    """
        The function congratulates the user.
        :return: none
    """

    global game_number

    game_number = game_number + 1

    return game_number


# ==============================================================================
# PROCESS
# ==============================================================================

# Main function
if __name__ == '__main__':
    start_the_finder()
