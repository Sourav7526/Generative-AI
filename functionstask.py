# function questions 





# def average_marks(*a):
#     total = 0
#     count = 0
#     for mark in a:
#         if mark >= 0:
#             total = mark+total
#             count = 1+count
#     if count == 0:
#         return 0
#     else:
#         return total / count

# print(average_marks(22,33,44,55))


#user input 

# <----------->
# score=(input("Enter marks"))
# marks=[]
# for s in score.split():
#     marks.append(int(s))

# result=average_marks(*marks)
# print(result)



# def filter_details(**b):
#     for key, value in b.items():
#         if type(value) == str:
#             print(key, "=", value)
# filter_details(name="Sourav", age=21, city="ptk")
