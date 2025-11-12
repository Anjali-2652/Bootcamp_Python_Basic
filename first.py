import keyword
print(keyword.kwlist)  # this prints list of python keywords



"""this is the
program which checks voting eligibility"""
age = 18 
if age >= 18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")


# this prints the name i give to input 
# name = input("Enter your name:")
# print("Hello!!" +  name)

# datatypes 
# 1. dictionary.................
data = {
    101: "anjali",
    102: "raj",
    103: "raman"
}
print(type(data))
print(data[101])

roll = {    
    "anjali": 10,
    "ram": 11,
    "shyam": 12
}

print(roll['anjali'])

# and or not  boolean
x = 10 
print(x<5 and x<10)

# 2. set........................we can not do indexing here not print its data in order...........
data = {10, 20, 30, "python"}
print(data)
empty = {}
print(type(empty))

a = 'python\n is a "programming" language'
print(a)

b = r'python\n is a "programming" language'
print( r'python\n is a "programming" language')

# 3. list......................... 
data = [-50, 10, 20, 15, "anjali"]
data[1] = 30
print(data)
print(type(data))
print(data[1])
data.append("ram")
print(data)
data.remove("ram")
print(data)
data.insert(2, "ram")
print(data)
# data.clear()
# print(data)
data.remove("ram")
print(data)

# sort ...........
number = [20, 10, 4, 3, 29, 100]
#number.sort()
#print(number)
number.sort(reverse=True)
print(number)

# tuple............
data = 10, 20, 3, 4, "anjali"
print(type(data))
print(data[1])


"""tuple is immutable we cannot change the value of tuple but we can change
the value of nested tuple like list inside tuple"""

abc = (1, 2, [3,4,5], 6,7)
abc[2][2]= 0
print(abc)

a, b, c = 1,3, 5
print(a)
print(type(a))

for i in range(10, 20, 2):
    print(i)

abc = range(30, 10, -3)
print(abc)
print(list(abc))

# operator.......................

# assignment operator....
a = 21
b=10
if(a==b):
    print("a is equal to b")
else:
    print("a is not equal to b")

if(a!=b):
    print("a is not equal to b")
else:
    print("a is equal to b")

if(a<b):
    print("a is less than b")
else:
    print("a is greater than b")


if(a>b):
    print("a is greater than b")
else:
    print("a is less than b")

if(a>=b):
    print(" a is greater than equal to b")

else:
    print("a is not greater than equal to b")


# logical operator..............
#bitwise operator...
print(60 ^ 13)

# type conversion..........
# implicit type conversion
num_int = 123
num_str = "456"
print("data type of num_int:", type(num_int))
print("data type of num_str", type(num_str))

num_str = int(num_str)

num_sum = num_int + num_str
print(num_sum)

name = input("enter your number:")
print("Hello", name)



print("...................../task/..................................")
a= "Expression"
print(a[::2])
print(a[:])
print(a[-2:3:-1])
print(a[-3:4])
print(a[-3:-4:-1])
print(a[-3:7:-2])
print(a[1:-8])
print(a[9::-10])
print(a[9:-10:-1])
print(a[11::-6])
print(a[2:-15:-1])
print(a[-15::-2])
print(a[7:-1])
print(a[-1:0:])
print(a[:-1:])
print(a[::-1])
print(a[-1:7])
a="123abc"
b=a.maketrans("abc","abc")
print(b)

a="SoftwarIca College"
print(a.istitle())
a="PYThON"
print(a.isupper())
a="capital"
print("A".isupper())
a="capital"
print(a.capitalize("c"))
a="+Capital9"
print(a.count("9"))

#............condition...................

#....if-else............
print("..............condtition........................")
a = int(input("enter the number"))
if a==100:
    print("U R intelligent")
else:
    print("not satisfied")



#......elif..................
marks = int(input("enter the marks:"))
if (marks >= 90 and marks <= 100):
    print("U R graded by A+")
    print("excellent")
elif (marks >=80 and marks <=90):
    print("U R graded by A")
    print("best")
elif (marks >=70 and marks <=80):
    print("U R graded by B+")
    print("good")
elif (marks >=60 and marks <=70):
    print("U R graded by B")
    print("not bad")
else:
    print("U need to hardwork")
    print("satisfactory")

#password and username checking

username = input("enter your username:")
password = input("enter your password:")

if username == "admin":
    if password == "password":
        print("login successful! welcome,admin")
    elif password == 12345:
        print("weak password, please try strong password")
    else:
        print("Incorrect password!!")

if username == "guest":
    if password == "password":
        print("login successful, welcome guest")
    elif password == "abcde":
        print("weak password, please try strong password")
    else:
        print("Incorrect password!!")
    
else:
    if password == "password":
        print("login successful, welcome user")
    elif password == 12345:
        print("weak password")
    else:
        print("Incorrect password")