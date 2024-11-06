# inet_4031_adduser_script
This is an adduser Python script for assignment 9, of INET 4031. 


Here’s an expanded README that incorporates your additional instructions:

INET4031 Add Users Script and User List
# Overview
In server administration, automation is essential, especially when managing a large number of servers. Tasks like user creation can be automated using various tools, including BASH, PERL, and Python. This assignment focuses on using Python for command line automation to create multiple users efficiently.

# Program Description
This program, create-users.py, automates the process of creating new users on a Linux server. The script reads user information from an input file (create-users.input), validates each entry, and creates the user with specified properties like username, group, and home directory. This is especially useful in environments where adding many users consistently and accurately is necessary.

# Program Files
create-users.py: The Python script responsible for reading the user data and creating users.
create-users.input: The input file containing the list of users to be created.

# How to Run the Code
To run the script, ensure the following requirements are met:

You have sudo privileges on a Linux server.
You have Python installed on the server.
You have prepared the create-users.input file with the desired user information.

# Instructions:
Download the script: Clone the GitHub repository or copy create-users.py to your server.
Prepare the Input File: Create create-users.input in the same directory as the script. Format each line like this:
