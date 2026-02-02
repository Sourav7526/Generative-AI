from os import name


# dict={}
# n=int(input("Enter how many keys value you want "))
# for i in range(n):
#     key=input("enter key :")
#     value=input("enter value :")
#     dict[key]=value
# print(dict)    



employee_details = {
    101: {"name": "Alice", "department": "HR", "salary": 60000},
    102: {"name": "Bob", "department": "IT", "salary": 45000},
    103: {"name": "Charlie", "department": "Finance", "salary": 75000},
    104: {"name": "Diana", "department": "Marketing", "salary": 50000}
}
high_salary=[]
for details in employee_details.values():
    if details["salary"]>50000:
        high_salary.append(details["name"])
print(high_salary)



