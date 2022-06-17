#n= int(input("enter a number:"))
#while n>=1:
 #   r=n%10
  #  print(r,end="")
   # n=n//10
from setuptools._distutils.command.install_data import install_data

mil=['df',3333]
num = [1,2,2,5,6,7,7,3,4,56,77]
num.insert(2,555)
num.append(44)
num.remove(77)
num.pop(0)
print(num);
del num[2:]
print(num);

print(num);
print(min(num))
print(sum(num))

tup=(21,26,48,25,25)
print(tup)
print(tup.count(25))

set={22,25,14,21,5,5,5}
print(set)

print(help('list'))
var1 = 5;
print(id(var1))
name="vipina"
print(id(name))
var2=10;
var3 = 10;
var2=var1;
print(id(var2))
print(id(var3))
print(id(10))
dict = {'arun':22,'kiran':'33'}
print(dict)
a=5;
b=4;

print(a<8 and b<5);
print(bin(25))
print(~14)

n = int(input("enter a number:"))
m=1
for x in range(m,n+1):
    m = m*x

print(m)