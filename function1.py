def add(numbers):
    sum=0
    for x in numbers:
        sum+=x
    return sum
print(add((1,2,3,4)))


def subtract(values):
    first=0
    for x in values:
        first-=x
    return first
print(subtract((10,5)))

def multiplication(numbers):
    a=1
    for x in numbers:
        a*=x
    return a
print(multiplication((2,4)))


