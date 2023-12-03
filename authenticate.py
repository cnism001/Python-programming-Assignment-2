import sys

# Usually we would use database but here lists are used to store users
users = ["user1", "user2", "user3"]
passwords = ["pass1", "pass2", "pass3"]

# authentication function
# returns : userid as an integer
# return value -1 means that user was not found
def authenticate(username, password) -> int:
    # Userid is used after the login to identify user
    userid = 0

    # Loop to authenticate user
    for u in users:
        # TODO: test prints
        # print(u)
        if u == username:
            if password != passwords[userid]:
                return -1
            else:
                return userid
        userid += 1

    # User was not found.
    return -1

# main function
def main() -> int:
    username = input("username: ")
    password = input("password: ")
    result = authenticate(username, password)
    print(result)
    if result >= 0:
        #Authentication was successful
        return 0
    else:
        #Authentication failed
        return 1

# main function entry point
if __name__ == '__main__':
    sys.exit(main())