#Prime number
n = int(input("Enter number: "))

if n < 2:
    print(False)
else:
    for i in range(2, n):
        if n % i == 0:
            print(False)
            break
    else:
        print(True)

#Pallindrome
a = input("Enter a string: ")
if a == a[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#Table
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} X {i} : {n*i}")

