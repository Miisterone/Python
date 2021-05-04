# ==============================================================================
# IMPORTS
# ==============================================================================

import random

# ==============================================================================
# GLOBAL VARIABLE
# ==============================================================================


internal_number = None
internal_upper_limit = 1000
internal_lower_limit = 0
r = 0
demo = 0


# ==============================================================================
# SUB FUNCTIONS
# ==============================================================================

def set_internal_number(number):
    # This function sets the value of internal_number
    global internal_number
    internal_number = number


def get_internal_number():
    return internal_number


def set_internal_upper_limit(upper_limit):
    global internal_upper_limit
    internal_upper_limit = upper_limit


def get_internal_upper_limit():
    global internal_upper_limit
    if demo == 2:
        internal_upper_limit = 150
    return internal_upper_limit


def set_internal_lower_limit(lower_limit):
    global internal_lower_limit
    internal_lower_limit = lower_limit


def get_internal_lower_limit():
    global internal_lower_limit
    if demo == 2:
        internal_lower_limit = 100
    return internal_lower_limit


def random_number():
    global r
    r = random.randint(internal_lower_limit, internal_upper_limit)
    return r

# ==============================================================================
# PROCESS
# ==============================================================================

# Main function
if __name__ == '__main__':
    random_number()
    print("/================================================")
    print("| Original internal number is: '{}'".format(get_internal_number()))
    print("| Original internal upper limit is: '{}'".format(get_internal_upper_limit()))
    print("| Original internal lower limit is: '{}'".format(get_internal_lower_limit()))
    print("|================================================")
    print("| Generated internal number with default limit is: '{}'".format(random_number()))
    print("\\================================================")

    print("\n")

    demo = 2
    print("/================================================")
    print("| Original internal upper limit is: '{}'".format(get_internal_upper_limit()))
    print("| Original internal lower limit is: '{}'".format(get_internal_lower_limit()))
    print("|================================================")
    print("| Generated internal number with default limit is: '{}'".format(random_number()))
    print("\\================================================")
