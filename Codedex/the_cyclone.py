# Logical operators, also known as Boolean operators, combine and evaluate two conditions. They are and, or, and not operators:

# and returns True if both conditions are True, and returns False otherwise.
# or returns True if at least one of the conditions is True, and False otherwise.
# not returns True if the condition is False, and vice versa.

# So you might be wondering: and and or are awfully similar, how do I remember the differences between the two? Let's break this down in a table form:

# A	B	A and B	A or B
# False	False	False	False
# False	True	False	True
# True	False	False	True
# True	True	True	True

height = int(input("How tall are you?  "))
credit = int(input("How much credit do you have?  "))



if height >= 137 and credit >= 10:
    print("Enjoy the ride")
elif height < 137 or credit >= 10:
    print("You are not tall enough to ride")
elif credit < 10 and height >= 37:
    print("You don't have enough credits")
else :
    print("You don't meet the requirments")


