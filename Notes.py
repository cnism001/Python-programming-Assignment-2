# notes.py - Simple notes application

# modules
import sys
import datetime
import getpass
import authenticate
import memorydatabase as database

# main function
def main() -> int:
    # Main loop will run as long as username is not empty.
    while (True):
        # userid is set initially to -1. In this app it means that user is not authenticated.
        userid = -1

        # Login loop
        while (userid == -1):
            print("\nLogin or just press enter to exit the application.\n")
            username = input("Username: ")
            # Exit main function and application if username is empty
            if (username == ""):
                return 0
            password = getpass.getpass()
            userid = authenticate.authenticate(username, password)

        # Empty line
        print()

        # Main menu
        onmainmenu = True
        while (onmainmenu):
            print("Main menu:")
            print("1. Create a note")
            print("2. Retrieve notes")
            print("3. Logout")

            try:
                choice = int(input("Choose and press enter: "))
            except ValueError:
                # if input is not a number
                choice = -1

            # Create a new note
            if int(choice) == 1:
                # Ask for details
                subject = input("Subject: ")
                text = input("Text: ")

                # Initially result is set to -1
                result = -1
                # Create a new note
                result = database.createnote(userid, subject, datetime.datetime.now(), text)
                # Print the result
                print("New note created: " + str(result))

            # List notes of current user and open a new menu to access them
            elif int(choice) == 2:
                # Request list of notes
                usernotes = database.listusernotes(userid)

                # List number
                number = 0

                # Fetch details of each note and show them in menu
                for n in usernotes:
                    print(str(number) + ". " + database.notedetails(n)["subject"])
                    number += 1
                try:
                    selectednote =  int(input("Enter a number of a note of any other number to exit: "))
                except ValueError:
                    # if input is not a number
                    selectednote = -1

                # Show details of one note and show note specific menu
                selectednote =  input("Enter a number of a note of any other number to exit: ")
                if ((int(selectednote) < len(usernotes)) and (int(selectednote) >= 0)):
                    note = database.notedetails(usernotes[int(selectednote)])
                    print("--- --- ---")
                    print("Subject: " + note["subject"])
                    print("Date: " + str(note["date"]))
                    print("Text: " + note["text"])
                    print("--- --- ---")
                    # One new menu loop that is used to delete menu item
                    choice = input("Type \"Delete\" to delete this note or press enter to go back: ")

                    if (choice == "Delete"):
                        database.deletenote(usernotes[int(selectednote)])
                        # Reset choice variable as it is used in other menus
                        choice = 0
                    else:
                        # Reset choice variable as it is used in other menus
                        choice = 0

                else:
                    # Reset choice variable as it is used in other menus
                    choice = 0

            # Rest of the answers will log user out
            else:
                onmainmenu = False
            
    # Exit successfully
    return(0)

# main function entry point
if __name__ == '__main__':
    sys.exit(main())