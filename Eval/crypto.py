# ==============================================================================
# GLOBAL VARIABLE
# ==============================================================================

check = False
check2 = False
original = ""


# ==============================================================================
# SUB FUNCTIONS
# ==============================================================================

def encrypt_message():
    #I present you my encryption. It is called "Where is the m".

    """
        This function replaces some characters of the given message with numbers.

        :return: None
    """
    if check == False:
        text = input("| What is the message to translate:")
        for char in text:
            if char == 'm':
                text = text.replace('m', '.')
            elif char == 'M':
                text = text.replace('M', '!')
            else:
                pass
        print("| Converted message is:")
        print("| =>", text)
    if check == True:
        global original

        for char in original:
            if char == 'm':
                original = original.replace('m', '.')
            elif char == 'M':
                original = original.replace('M', '!')

def decrypt_message():
    """
        This function replaces the numbers in the message with the original letters

        :return: None
    """
    if check2 == False:
        text = input("| What is the message to translate:")
        for char in text:
            if char == '.':
                text = text.replace('.', 'm')
            if char == '!':
                text = text.replace('!', 'M')
            else:
                pass
        print("| Converted message is:")
        print("| =>", text)
    if check2 == True:
        global original

        for char in original:
            if char == '.':
                original = original.replace('.', 'm')
            if char == '!':
                original = original.replace('!', 'M')

# ==============================================================================
# PROCESS
# ==============================================================================

if __name__ == '__main__':
    print("/===")
    original = input("| Original Crypto message:")
    check = True
    encrypt_message()
    print("\\===")

    print("")
    print("/===")
    print("| Encrypted Crypto message:",original)
    print("\\===")

    print("")
    print("/===")
    check2 = True
    decrypt_message()
    print("| Decrypted Crypto message:", original)
    print("\\===")