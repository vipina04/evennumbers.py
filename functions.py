#def fun():
 #   print("hello")
#fun()
#def function(*x):
 #   print("hello",x)
#function("world","hai","how","are","you")

#def fnctn(**x):
  #  print("values",x)
#fnctn(name="vipina",Age=99,address="abc")


def multiply(numbers):
    total=1
    for x in numbers:
      total*=x
    return total
print(multiply((1,2,3,4,5,6,7)))
