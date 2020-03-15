# -----------------------------------------+
# Faith Nelson                             |  
# CSCI 107, Assignment 2                   |
# Last Updated: September 13, 2018         |  
# -----------------------------------------|
# This will print out a customized         |
# "buisness" card including the users name,|
# work number, and specified email. For    |
# this assignment we have assumed the      |
# person's first name has no more than     |
# 9 characters,the person's last name has  |
# no more than 10 characters, and the      |
# person's telephone number is entered in  |
# the format (xxx)-xxx-xxxx where x is a   |
# digit between 0 and 9.                   |  
# -----------------------------------------+


firstName = input("Please enter your first name > ")
lastName = input("Please enter your last name > ")
phoneNumber = input("Please enter your telephone number > ")
fullName = (lastName + ", "+ firstName)

nameLength = len(fullName)

email = (firstName.lower() + "@parasail.com")

print(" ")
print("Here is your business card ...")
print(" ")
print("+------------------------------------------------+")
print("|    |                                           |")
print("|   -|          "    + fullName.ljust(33) + "|")
print("|  --|          Tribute Liabilities Associate    |")
print("| ---|          Parasail Capital                 |")
print("| ---------                                      |")
print("|  -------      4 Hunger Plaza                   |")
print("|               STE 1400                         |")
print("|               District 12, Panem 00012         |")
print("|                                                |")
print("| Work: "  +phoneNumber+"  @:"+ email.ljust(23) + "|")
print("+------------------------------------------------+")

