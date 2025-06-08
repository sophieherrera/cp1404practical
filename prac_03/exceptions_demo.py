"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
#
# When will a ValueError occur?
# When the user enters something that can not be converted into an not integer.
#
# When will a ZeroDivisionError occur?
# When the user enters zero.
#
# Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes, by checking if the denominator is zero before performing the division.