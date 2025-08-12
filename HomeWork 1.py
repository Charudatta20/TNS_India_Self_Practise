#Write a Python program to print numbers from 1 to 10 using a while loop.
a=1
while a<=10:
    print(a)
    a+=1


#The second program takes a number as input and reverses it using a while loop
num=int(input("enter a number: "))
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print("the reverse of the number is: ",rev)
  


#The third program implements a password checker that keeps asking for input until the correct password "admin123" is entered
password = "admin123"
while True: 
    input=input("Enter the password: ")
    if input==password:
        print("Access Granted")
    else:
        print("Access Denied, Try Again")
