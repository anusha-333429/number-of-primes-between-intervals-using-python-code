#Write a program to find prime numbers between two intervals
a=int(input("enter lower limit"))
b=int(input("enter upper limit"))
c=0
for i in range(a,b+1):
    for j in range(a,i):
        if(i%j==0):
             break
    else:
        print(i)








