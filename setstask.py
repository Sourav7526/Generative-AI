#set questions

#question 1


# friday = {"Alice","Bob","Charlie"}
# saturday = {"Charlie", "David","Eve"}
# all_guests=friday.union(saturday)
# print(all_guests)
# both_nights=friday.intersection(saturday)
# print(both_nights)


#question 2
 

# data = [1, 2, 2, 3, 4, 4, 4, 5]
# clean_data=set(data)
# print(clean_data)

# clean_data.add(6)
# print(clean_data)


#question 3


# library_books = {"Hobbit","1984","Gatsby", "Odyssey", "Hamlet"}
# checked_out = {"1984", "Hamlet"}

# current_available=library_books.difference(checked_out)
# print(current_available)

# if "Don Quixote" not in library_books:
#     library_books.add("Don Quixote")
# else:
#     print("Already have")

# print(library_books)


#question 4

# user_permissions = {"read", "write"}
# admin_reqs = {"read", "write", "execute"}
# check=user_permissions.issubset(admin_reqs)
# print(check)
# missing=admin_reqs.difference(user_permissions)
# print(missing)



#question 5

# logs = {
# "404": [10, 12, 15, 20],
# "500": [12, 20, 22, 25],
# "403": [10, 20, 30]
# }
# all_errors=set(logs["404"]).intersection(logs["500"],logs["403"])
# print(all_errors)

# critical_servers=set(logs["500"]).difference(logs["404"])

# print(critical_servers)





