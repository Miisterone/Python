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
    """
        This function replaces some characters of the given message with numbers.

        :return: None
    """

    if check == False:
        text = input("| What is the message to translate:")
        for char in text:
            if char == 'a':
                text = text.replace('a', '4')
            elif char == 'b':
                text = text.replace('b', '8')
            elif char == 'e':
                text = text.replace('e', '3')
            elif char == 'l':
                text = text.replace('l', '1')
            elif char == 'o':
                text = text.replace('o', '0')
            elif char == 's':
                text = text.replace('s', '5')
            elif char == 't':
                text = text.replace('t', '7')
            else:
                pass
        print("| Converted message is:")
        print("| =>",text)

    if check == True:
        global original

        for char in original:
            if char == 'a':
                original = original.replace('a', '4')
            elif char == 'b':
                original = original.replace('b', '8')
            elif char == 'e':
                original = original.replace('e', '3')
            elif char == 'l':
                original = original.replace('l', '1')
            elif char == 'o':
                original = original.replace('o', '0')
            elif char == 's':
                original = original.replace('s', '5')
            elif char == 't':
                original = original.replace('t', '7')

def decrypt_message():
    """
        This function replaces the numbers in the message with the original letters

        :return: None
    """

    if check == False:
        text = input("| What is the message to translate:")
        for char in text:
            if char == '4':
                text = text.replace('4','a')
            elif char == '8':
                text = text.replace('8','b')
            elif char == '3':
                text = text.replace('3','e')
            elif char == '1':
                text = text.replace('1','l')
            elif char == '0':
                text = text.replace('0','o')
            elif char == '5':
                text = text.replace('5','s')
            elif char == '7':
                text = text.replace('7','t')
            else:
                pass
        print("| Converted message is:")
        print("| =>", text)

    if check == True:
        global original

        for char in original:
            if char == '4':
                original = original.replace('4', 'a')
            elif char == '8':
                original = original.replace('8', 'b')
            elif char == '3':
                original = original.replace('3', 'e')
            elif char == '1':
                original = original.replace('1', 'l')
            elif char == '0':
                original = original.replace('0', 'o')
            elif char == '5':
                original = original.replace('5', 's')
            elif char == '7':
                original = original.replace('7', 't')

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