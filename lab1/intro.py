print('Hello World')

name = 'Gabe'
last_name = 'Seabaugh'
age = 27
found = False
average = 42.23

print(name)
print(last_name)
print(age)
print(found)
print(average)

print(21 + 12)
print(age - average)
print(846 * 293)
print(522 / 6)

def test():
    print("inside the function")
    print("this too")
print('outside the function')

def separator():
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')

test()

separator()

print(name + last_name)

separator()

if(age < 90 ):
    print('You are young')
elif(age == 90):
    print('you are borderline')
else:
    print('You are old')
