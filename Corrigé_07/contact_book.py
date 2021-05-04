#!/usr/bin/env python3
# coding: utf-8
# ##############################################################################
# Description:  This POO allow to manage a contact book.
#
# Required:     - Run as Standard User.
#               - Python 3.x
#
# Goals:        - Utilisation de la Programmation Orientée Objet
#               - Utilisation du module "pickle" pour la sauvegarde
#               - Utilisation du module "re" pour la comparaison par
#                 RegExp pattern
#               - Il n’y a plus de variable globale
#               - Mise en place de 3 classes agréées entre elles
#               - Mise en place d’un héritage pour sécurisé
#                 les entrées utilisateur
#               - "DataChecker"
#                 - Initialisation de la variable interne
#                 - Vérification de la conformité de la valeur donnée
#                   en fonction de la pattern donnée
#                 - Récupération du résultat de la dernière comparaison
#               - "ContactInformation"
#                 - Initialisation des informations du contact
#                   - Ajout des patterns pour chaque entrée utilisateur
#                     - "Nom de famille" => Tout en majuscule
#                     - "Prénom" => Première lettre en majuscule,
#                       le reste en minuscule
#                     - "Date de naissance" => (mois)/(jour)/(année sur 4 digit)
#                     - "Email" => xxx@yyy.zzz
#                   => Saisie sécurisée
#                 - Récupération des informations du contact
#               - "ContactBook"
#                 - Initialisation du carnet de contact
#                 - Ajout d’un nouveau contact
#                 - Récupération de la liste des contacts
#                 - Sauvegarde de la liste des contacts dans un fichier
#               - "ControllerBook"
#                 - Menu interactif pour les actions utilisateur
#                 - Ajout d’un contact
#                 - Listing des contacts existants
#                 - Sortie de l’application
#               - Le bloc main ne doit faire que 2 actions
#                 - Initialisation d’une instance de classe " ControllerBook"
#                 - Lancer le menu interactif
#                 - Ajout des patterns pour chaque entrée utilisateur
#                 => Saisie sécurisée
#               - Initialisation de l’instance de classe " ControllerBook"
#                 - Doit récupérer la sauvegarde (si existante)
#                   avant de créer une nouvelle instance
#               - Menu interactif
#                 - La sauvegarde du carnet doit être faite
#                   après la création d’un nouveau contact
#                 - Le seul moyen de sortir du menu interactif
#                   est de quitter l’application
#               - Print, Questions et mise en forme
#                 - Aucun des trois dans la classe "ContactBook"
#                 - Seul les demandes d’informations contact à l’utilisateur
#                   et ses messages d'erreurs associés doivent être présents
#                   dans "ContactInformation"
#
# Author:       DESTOMBES Matthieu
#
# Date:         2021.03.23
# ##############################################################################

# ==============================================================================
# IMPORTS
# ==============================================================================

import re
import pickle
import os


# ==============================================================================
# CLASS MANAGEMENT
# ==============================================================================

class DataChecker(object):
    """
    This class allow program to manage safely input data.

    """

    def __init__(self):
        """
        Class DataChecker constructor with following actions:
        - Initialize internal attributes.

        Returns:
            Self

        """

        self.__value_match = None

    def check_expected(self, value, pattern):
        """
        This method allow program to check value content with
          given Regexp pattern.

        Args:
            value: String - Value content to check with linked pattern.
            pattern: String - Regexp linked pattern.

        Returns:
            Boolean - The result check. True if it's OK.
                      False, otherwise.

        """

        self.__value_match = bool(re.match(pattern, value))

        return self.__value_match

    def get_last_check_result(self):
        """
        This method allow program to get the result of last previous check.

        Returns:
            Boolean - The previous result check. True if it's OK.
                      False, otherwise.

        """

        return self.__value_match


class ContactInformation(DataChecker):
    """
    This class allow program to manage information details about one Contact.

    """

    def __init__(self):
        """
        Class ContactInformation constructor with following actions:
        - Initialize internal attributes,
        - Ask to user the contact information.

        Returns:
            Self

        """

        # Calling of parent initialization
        super().__init__()

        # Question definition
        self.__first_name_question = \
            "| What is the first name of the user: "
        self.__last_name_question = \
            "| What is the last name of the user: "
        self.__birthday_question = \
            "| What is the birth date of the user (MM/DD/YYYY): "
        self.__email_question = \
            "| What is the email of the user: "

        # Contact first name safe initialization
        self.__first_name = input(self.__first_name_question)
        self.__bad_first_name = "| First name start with upper case\n" + \
                                "|   and follower by lower case..."
        self.__first_name_pattern = "^([A-Z][a-z]+)+$"
        while not self.check_expected(
            self.__first_name,
            self.__first_name_pattern
        ):
            print(self.__bad_first_name)
            self.__first_name = input(self.__first_name_question)

        # Contact last name safe initialization
        self.__last_name = input(self.__last_name_question)
        self.__bad_last_name = "| Last name is in upper case..."
        self.__last_name_pattern = "^([A-Z]+)+$"
        while not self.check_expected(
            self.__last_name,
            self.__last_name_pattern
        ):
            print(self.__bad_last_name)
            self.__last_name = input(self.__last_name_question)

        # Contact birthday safe initialization
        self.__birthday = input(self.__birthday_question)
        self.__bad_birthday = \
            "| There is an error in date format (MM/DD/YYYY)..."
        self.__birthday_pattern = "^(0[1-9]|1[0-2])/(0[1-9]|[1|2][0-9]|3[0-1])/(19|20)\d\d$"
        while not self.check_expected(
            self.__birthday,
            self.__birthday_pattern
        ):
            print(self.__bad_birthday)
            self.__birthday = input(self.__birthday_question)

        # Contact email safe initialization
        self.__email = input(self.__email_question)
        self.__bad_email = \
            "| There is an error in date format (xxx@yyy.zzz)..."
        self.__email_pattern = \
            "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*)@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        while not self.check_expected(
            self.__email,
            self.__email_pattern
        ):
            print(self.__bad_email)
            self.__email = input(self.__email_question)

    def get_contact(self):
        """
        This method allow program to get all information about current contact
          saved into instance of Class ContactInformation.

        Returns:
            Tuple - (First name, Last name, Birthdate, Email)

        """

        return (
            self.__first_name,
            self.__last_name,
            self.__birthday,
            self.__email
        )


class ContactBook(object):
    """
    This class allow program to manage one Book of contacts.

    """

    def __init__(self, linked_file):
        """
        Class ContactBook constructor with following actions:
        - Initialize internal attributes.

        Returns:
            Self

        """

        self.__linked_file = linked_file
        self.__people = []

    def add_someone(self):
        """
        This method allow program to add new contact information detail to
          the current Book of contacts.

        Returns:
            None

        """

        self.__people.append(
            ContactInformation()
        )

    def contact_list(self):
        """
        This method allow program to get the list of all contacts saved in
          the current Book of contacts.

        Returns:
            List - The list of all contact. Contact in Tuple format as
                   (First name, Last name, Birthdate, Email)

        """

        return self.__people

    def save_book(self):
        """
        This method allow program to save the data content by
          the current Book of contacts into specific pickle file.

        Returns:
            None

        """

        pickle.dump(self, open(self.__linked_file, 'wb'))


class ControllerBook(DataChecker):
    """
    This class allow program to manage Book of contacts, by interactive command,
      as:
    - Reading,
    - Adding contact,
    - Saving data.

    """

    def __init__(self):
        """
        Class ControllerBook constructor with following actions:
        - Initialize internal attributes,
        - Make safe aggregation with ContactBook.

        Returns:
            Self

        """

        # Calling of parent initialization
        super().__init__()

        # Save file info block
        self.__save_filename = \
            "contact_book.dat"
        self.__saved_file_message = \
            "| Contact book saved with new contact!"
        self.__loaded_success_file_message = \
            "| Local file of contact book loaded!"
        self.__loaded_fail_file_message = \
            "| Local file of contact not founded...\n" +\
            "| Starting with empty book!"

        # Management of aggregation with ContactBook class
        self.__controlled_book = self.__load_book()
        if self.__controlled_book is None:
            self.__controlled_book = ContactBook(self.__save_filename)

        # Main instruction management
        self.__main_instruction = [
            "|",
            "| Contact Book Application",
            "|",
            "|======================================",
            "| Make your choice from the followings actions!"
        ]
        self.__available_actions = {
            'add': {
                'select': "A",
                'display': "adding a new contact"
            },
            'list': {
                'select': "L",
                'display': "listing all contact"
            },
            'quit': {
                'select': "Q",
                'display': "quit the application.."
            }
        }
        self.__action_available_pattern = "^[{0}]$".format(
            "|".join(
                [
                    self.__available_actions[key]['select']
                    for key in self.__available_actions.keys()
                ]
            )
        )
        self.__action_available_selection_question = \
            "| Select your action: "

        # Adding contact message
        self.__add_contact_header = \
            "| New contact to add..."

        # Application quit message
        self.__quit_application_question = \
            "| Do you really wish quit the application (Y/N)? "
        self.__quit_application_pattern = \
            "[Y|N]"

        # Generic bas answer management
        self.__bad_answer = \
            "| Please enter a correct answer!"

        # Contact list display management
        self.__list_contact_header = \
            "| First name           | Last name            " + \
            "| Birthdate  | E-mail"
        self.__list_contact_line_format = \
            "| {0:<20} | {1:<20} | {2:<10} | {3:<30}"

    def __load_book(self):
        """
        This method allow program to load the data content to
          the current Book of contacts from specific pickle file.

        Returns:
            ContactBook - Saved content of older Book of contacts.
                          None of no saved file founded.

        """

        # Initialization of return value
        loaded_book = None

        # Display of loading block
        print("\n/======================================")
        if os.path.isfile(self.__save_filename):
            # Get content from file if exist
            print(self.__loaded_success_file_message)
            loaded_book = pickle.load(open(self.__save_filename, 'rb'))

        else:
            # Display the file is not exist
            print(self.__loaded_fail_file_message)

        print("\\======================================")

        # Return the founded class
        return loaded_book

    def __add_contact(self):
        """
        This method allow program to add contact into the current
          Book of contacts and saved content.
        Each needed information should be ask to user...

        Returns:
            None

        """

        # Display new contact block
        print("\n/======================================")
        print(self.__add_contact_header)
        print("|======================================")

        # Add new contact management
        self.__controlled_book.add_someone()
        print("|======================================")

        # Saved the new content
        self.__controlled_book.save_book()
        print(self.__saved_file_message)
        print("\\======================================")

    def __list_contact(self):
        """
        This method allow program to displayed a format list of all contact
          saved in the current Book of contacts.

        Returns:
            None

        """

        # Display list contact block
        print("\n/======================================")
        print(self.__list_contact_header)

        # Display format each contact saved
        for current_contact in self.__controlled_book.contact_list():
            contact_info_details = current_contact.get_contact()
            print(self.__list_contact_line_format.format(
                contact_info_details[0],
                contact_info_details[1],
                contact_info_details[2],
                contact_info_details[3]
            ))

        print("\\======================================")

    def __quit_application(self):
        """
        This method allow program to make a safe quit of the application.

        Returns:
            Boolean - True if quit if confirmed.
                      False otherwise.

        """

        # Initialization of return value
        quit_answer_valid = None

        # Display of quitting block
        print("\n/======================================")
        # Ask of the confirmation
        confirmation = input(self.__quit_application_question).upper()
        # Loop until bad answer
        while not self.check_expected(
            confirmation,
            self.__quit_application_pattern
        ):
            print(self.__bad_answer)
            confirmation = input(self.__quit_application_question).upper()
        print("\\======================================")

        # Check expected answer
        if confirmation == 'Y':
            # Set as valid answer he return
            quit_answer_valid = True

        elif confirmation == 'N':
            # Set as valid answer he return
            quit_answer_valid = False

        # Return the valid user choice
        return quit_answer_valid

    def __display_instruction(self):
        """
        This method allow program to display properly format the instruction
          of application.

        Returns:
            None

        """

        # Display header information block
        for line_instruction in self.__main_instruction:
            print(line_instruction)

        # Display all available action
        for key in self.__available_actions.keys():
            print(
                "| {0} - for {1}.".format(
                    self.__available_actions[key]['select'],
                    self.__available_actions[key]['display']
                )
            )

    def menu_management(self):
        """
        This method allow program to the application actions.
        Loop until the user make the choice of quit the application.

        Returns:
            None

        """

        # Initialization of first loop
        loop_lock = True

        # Loop until the user make the choice to quit
        while loop_lock:
            # Display new block of menu
            print("\n/======================================")

            # Display instruction
            self.__display_instruction()

            # Available action safe management
            user_selection = input(
                self.__action_available_selection_question
            ).upper()
            while not self.check_expected(
                user_selection,
                self.__action_available_pattern
            ):
                print(self.__bad_answer)
                user_selection = input(
                    self.__action_available_selection_question
                ).upper()

            print("\\======================================")

            # If add contact selected
            if user_selection == 'A':
                self.__add_contact()

            # If list contact selected
            elif user_selection == 'L':
                self.__list_contact()

            # If quit application selected
            elif user_selection == 'Q':
                loop_lock = not self.__quit_application()


# ==============================================================================
# PROCESS
# ==============================================================================

# Main function
if __name__ == '__main__':

    # Controller of book creation
    my_controller = ControllerBook()

    # Controller menu launching
    my_controller.menu_management()
