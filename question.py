n = int(input("Enter a number: "))

if n <= 1:
    print("Not prime")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")

#2 question

# n=input("enter a number ")
# if n == n[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")    



# #3 question

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
    #     print("fizzbuzz")
    # elif i % 3 == 0:
    #     print("fizz")
    # elif i % 5 == 0:
    #     print("buzz")
    # else:
    #     print(i)

