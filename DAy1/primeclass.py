num=int(input())
if num>=1:
    for i in range (2,num):
        if(num%1)==0:
            print(num,"is not a prime")
            break
else:
    print(num,"Is prime")
else:
    print("enter a number")
