#!/usr/bin/python3

# Importing modules for various tasks:
import os   # Used to execute system commands, such as adding users and setting passwords.
import re   # Used for regular expression matching, which helps identify lines to skip.
import sys  # Used to read from standard input, allowing the script to process lines directly from a file or input stream.

def main():
    for line in sys.stdin:

        # This regular expression checks if the line begins with a "#" character,
        # which typically indicates a comment in configuration files. Lines that match
        # this pattern will be skipped, as they do not contain user data.
        match = re.match("^#", line)
    
        print("The contents of the match variable were :", match)



        # Splitting the line by ":" and storing each part in the "fields" list.
        # Each line is expected to follow the format:
        # username:password:last_name:first_name:groups
        fields = line.strip().split(':')

        print("Length of the fields was: ", len(fields))

        # This IF statement checks two things:
        # 1. Whether the line is a comment (match is not None).
        # 2. Whether the line contains exactly five fields (fields length is 5).
        # If either condition is true, the line is skipped with "continue."
        # This statement relies on the `match` line to filter comments and the `fields` line
        # to check for the correct number of fields, ensuring each line is in the expected format.

        if match or len(fields) != 5:
            continue

        # Assigning variables to each field in the "fields" list for easy reference.
        username = fields[0]
        password = fields[1]
        # Creating the "gecos" field using the last_name and first_name values, formatted as "<last_name> <first_name>,,,"

        gecos = "%s %s,,," % (fields[3], fields[2])
        # Splitting the "groups" field by commas, to handle multiple groups.
        groups = fields[4].split(',')

        # Output message for account creation and constructing the command to add a user without a password.

        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        # print(cmd)
        os.system(cmd)

        # Output message for setting the password and constructing the command to set the user's password.
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        # print(cmd)
        os.system(cmd)

        # Looping through each group in the "groups" list to assign the user to the group.
        for group in groups:
            # Checking if the group is not a placeholder ("-").
            # If it is not "-", the user will be assigned to this group.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                # print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
