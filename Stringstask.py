# question 1 (to print first two and last two charters of a string)
# def given_string(s): # pyright: ignore[reportRedeclaration]
#     if len(s) < 2:
#         return "not a valid string"
#     return s[:2] + s[-2:]
# print(given_string("coder roots"))
# print(given_string("new year"))

# user_input = input("enter a string")
# result = given_string(user_input)
# print(result)


# # question 2 (to swap charcters of string)

# def swap_char(a, b):
#     return b[0] + a[1:] + " " + a[0] + b[1:]
# word1 = input("enter 1st word")
# word2 = input("enter 2nd word")
# result = swap_char(word1, word2)
# print(result)


# # # question 3 (add ing and ly)


# def given_string(s):
#     if len(s) < 3:
#         return s
#     if s.endswith("ing"):
#         return s[:-3] + "ly"
#     return s + "ing"
# str1 = input("enter a string")
# result = given_string(str1)
# print(result)


# # # question 4 (remove nth character)

# def remove(s, ind):
#     return s[:ind] + s[ind+1:]

# string = input("enter a string")
# index = int(input("enter index you want to remove"))

# result = remove(string, index)
#print(result) 
