a = input("enter input")
count1 = 0
count2= 0

for i in a:
    if(i.islower()):
        count1+=1
    elif(i.isupper()):
         count2=count2+1

print("the lowercase letters :")
print(count1)
print("uppercase letters:")
print(count2)

