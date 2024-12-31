print("Hello World")

#integer
a=1
b=2
print(a+b)
print(type(a))

#string
a="hello"
b="world"
print(a+" "+b)
print(type(a))

#integer_parse
a=1
b="2"
print(str(a)+b)
print(type(a))

#float
a=1.5
b=2.7
print(a+b)
print(type(a))

#tuple
a = (1,2,3,'hello')
print(a)
#a[7]=99
# print(a)
print(type(a))

#set
a = {1,2,3,"hello"}
print(a)
# a[0]=99
# print(a)
print(type(a))

#for
for i in range(9):
    print(i)

for i in range(10, 20):
    print(i)

for i in range(10, 20, 2):
    print(i)

for i in range(10, 20):
    a="ram"
    print(f"hello {a} {i}")

fruits = {'apple', 'banana', 'orange'}
for x in fruits:
    print(x)
    break
    continue

#while
count = 0
while(count<3):
    count = count + 1
    print(count)

#if
a=10
if a == 10:
    print("a is 10.")
else:
    print("a is not 10.")