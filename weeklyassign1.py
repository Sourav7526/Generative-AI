
import random 


#question 1


# for i in range(1,51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizzbuzz")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     else:
#         print(i)



#question 2
# for num in range(2, 101):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(num, end=" ")


# #3 question
# numbers=int(input("Enter your makrs: "))
# if numbers>100 or numbers<0:
#     print("invalid marks")
# elif numbers>=90:
#     print("GRADE A")
# elif numbers>=80:
#     print("GRADE B")
# elif numbers>=70:
#     print("GRADE C")
# elif numbers>=60:
#     print("GRADE D")
# else: 
#     print("GRADE F")



#4 question
# num=int(input("Enter number :"))
# for i in range(1,11):
#     print( num,"x",i, "=",num*i)



#question 5
# list=[(i**2) if i%2==0  else i for i in range(0,21)]
# print(list)

#question 6
# enter_year=int(input("Enter year you want to check :"))
# if (enter_year%4==0 and enter_year%100==0) or enter_year%400==0:
#     print("year is leap year")
# else:
#     print("year is not leap year")    

#question 7
# a = float(input("Enter side a: "))
# b = float(input("Enter side b: "))
# c = float(input("Enter side c: "))

# if a == b == c:
#         print("The triangle is Equilateral")
# elif (a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c == a*a):
#         print("The triangle is Right-angled")
# elif a == b or b == c or a == c:
#         print("The triangle is Isosceles")
# else:
#         print("The triangle is Scalene")




#question 8
# num=int(input("enter a number :"))
# if num>0:
#     print("number is positive")
# elif num<0:
#     print("number is negative")
# else:
#     print("number is zero")

#question 9 missing

# #question 10
# weight=int(input("Enter your weight in kgs :"))
# height=float(input("enter you height in metres :"))
# BMI=weight/(height**2)
# print(BMI)
# if BMI < 18.5:
#     print("Underweight")
# elif BMI<=25:
#     print("Normal weight")
# elif BMI<=30:
#     print("Overweight")
# else:
#     print("Obesity")

#question 11
# day=int(input("Enter day of week in numeric :"))
# if day==1:
#     print("Monday")
# elif day==2:
#     print("Tuesday")
# elif day==3:
#     print("Wednesday")
# elif day==4:
#     print("Thursday")
# elif day==5:
#     print("Friday")
# elif day==6:
#     print("Saturday")
# elif day==7:
#     print("Sunday")
# else:
#     print("Invalid Input")



#question 12
# value=int(input("Enter price of product :$"))
# if value>=1000:
#     print(" 10% Dicount Applied, Discount price=",value*0.9)
# elif value>=500 and value<1000:
#     print(" 5% Dicount Applied, Discount price=",value*0.95)
# else:
#     print("No Discount Applied")



#question 13
# n=int(input("Enter a Number"))
# sum=0
# for i in range(0,n+1):
#     sum+=i
# print(sum)



#question 14 dictionary




#question 15 
# str1=str(input("Enter a string :"))
# vowels="aeiouAEIOU"
# sum=0
# for j in vowels:
#     sum=sum+str1.count(j)
# print(sum)




#question 16

# num = input("Enter a number :")
# print(sum(int(i) for i in num ))

#question 17
# n=int(input("Enter a number"))
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()
# for i in range(n):
#     for j in range(n,i,-1):
#         print("*", end=" ")
#     print()




#question 18


# random_number = random.randint(1, 100)

# print("welcome to random number guess game :")
# while True:
#     guess = int(input("Enter your guess: "))

#     if guess < random_number:
#             print("Too low! Try again.")
#     elif guess > random_number:
#             print("Too high! Try again.")
#     elif:
#             print("Congratulations! You guessed the correct number.")
        



#question 19
# num=int(input("Enter a number"))
# for i in range(0,num+1):
#     if i%2==0:
#         print(i, end=" ")
    



# #question 20
# l=[int(input("Enter numbers")) for i in range(0,11)]
# print(l)
# #a
# if 25 in l:
#     print("25 is in the list")
# else:
#     print("25 is not in the list")
# #b
# print("Length of the list",len(l))

# #c
# print("Occurence of 25 in list", l.count(25))

# #d
# for i in l:
#     print(i)

# #e 
# for i in l:
#     if i%2==0:
#         print(i)




#question 21
# str=str(input("enter string of min 10 words and max 19 words"))
# words=str.split()
# if len(words)>10 or len(words)<19:
#     print("Invalid string")
# else:
#  print(str)
#  print(len(str))

# if str==str[::-1]:
#    print("String is pallindrome")
# else:
#    print("string is not palindrome")


# middle_word=len(words)//2
# print("Middle word is ", words[middle_word])


# print("Second last word is",words[-2])





#question 22

# print("Welcome to Calci:")
# print("1. Power")
# print("2. Sum")
# print("3. Sub")
# print("4. Multiple")
# choice=int(input("Enter your choice. -->"))
# if choice==1:
#     a=int(input("Enter 1st Number :"))
#     b=int(input("Enter power :"))
#     power=a**b
#     print("Ans is",power)
# elif choice==2:
#     a=int(input("Enter 1st Number :"))
#     b=int(input("Enter 2nd Number :"))
#     sum=a+b
#     print("Sum is",sum)
# elif choice==3:
#     a=int(input("Enter 1st Number :"))
#     b=int(input("Enter 2nd Number :"))
#     sub=a-b
#     print("Ans is",sub)
# elif choice==4:
#     a=int(input("Enter 1st Number :"))
#     b=int(input("Enter 2nd Number :"))
#     product=a*b
#     print("Multiple is",product)
# else:
#     print("Invalid Option Selected")




#question 23
# str=[(input("Enter string")) for i in range(0,5)]
# print(str)
# sum = 0
# for s in str:
#     if len(s) >= 2 and s[0] == s[-1]:
#         sum += 1
# print(sum)
