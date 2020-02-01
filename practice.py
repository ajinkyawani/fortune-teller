
numbers = [1,2,3,4]
print(numbers)
print(list(map(lambda x: x + 2, numbers)))

number_list = list(range(-5,5))
print(number_list)
greater_than_zero = list(filter(lambda x: x > 0, number_list))
print(greater_than_zero)

def add(x):
    return x +2

def wrapper(q, x):
    return q(x)

print(wrapper(add, 2))

t = (1,2,3,4,5,6)
string = "hello world"
print(string.split())