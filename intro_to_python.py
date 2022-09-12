def string_both_ends(str):
    if len(str)< 2:
        return ''
    return str[0:2] + str[-2:]

string = input("Enter your string:")
stringToReturn = string_both_ends(string)
print(stringToReturn)
