#1 PROBLEM



# name=str(input("enter your name"))
# age=int(input("enter your age"))

# print("choose a class")
# print("1. first class=1500")
# print("2. second class=1000")
# print("3. sleeper class=500")

# choice=int(input("enter your choice(1/2/3): "))
# if choice == "1":
#     ticket_price = 1500
#     travel_class = "First Class"
# elif choice == "2":
#     ticket_price = 1000
#     travel_class = "Second Class"
# elif choice == "3":
#     ticket_price = 500
#     travel_class = "Sleeper Class"

# if age<5:
#     ticket_price = 0
# elif age>=60:
#     ticket_price = ticket_price * 0.8


# meal = input("Do you want to add a meal? (yes/no): ")

# if meal == "yes":
#     ticket_price += 200
#     meal_status = "Meal Included"
# else:
#     meal_status = "No Meal"

# print("------TICKET SUMMARY-------")
# print("passenger name:",name)
# print("age:",age)
# print("travel class",travel_class)
# print("meal status",meal_status)
# print("final price",float(ticket_price))
# print("Enjoy your journey! 🎉")



#2 problem

# print("Welcome to Burger King 🍔!")
# print("menu")
# print("1. Whopper Burger - ₹150")
# print("2. Crispy Veg - ₹100 ")
# print("3. Crispy Veg - ₹120 ")
# choice=int(input("enter choice 1/2/3 :"))
# quantity=int(input("Enter Quantity"))
# if choice==1:
#     price=150
#     itemname="Whopper Burger"
# elif choice==2:
#     price=100
#     itemname="Crispy Veg "
# elif choice==3:
#     price=120
#     itemname="Chicken wings"
# else:
#     print("nothing added")
# bill=price*quantity
# discount=0
# coupon=input("Do you have a coupon code? (yes/no):" )
# if coupon == "yes":
#     print("APPLYING COUPON......")
#     code = input("Enter your coupon code: enter in capital letters")
#     if code == "KING50":
#         discount = bill * 0.5
#         print("Discount Applied: 50%")
#         coupon_status="YES"
#     elif code == "BK20":
#         discount = 20
#         print("Discount Applied: ₹20")
#         coupon_status="YES"
#     elif code == "NOCOUPON":
#         print("No discount applied")
    
# else:
#     print("No coupon applied")
#     coupon_status="NO"

# final_price = bill - discount
# print("------BILL DETAILS---------")
# print("Item:", itemname)
# print("Quantity:", quantity)
# print("coupon applied ",coupon_status)
# print("Final Price: ₹", final_price)
# print("Thanks for ordering at Burger King! 🍟")