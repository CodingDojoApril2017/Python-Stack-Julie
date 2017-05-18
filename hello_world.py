print "hello world!"
x = "Hello Python"
print x
y = 42
print y
"""
THis is supposed to allow us to comment across multiple lines as long as the triple quoted comment is not the first thing in your life You can use double or single quotes
"""
x = [1,2,3,4,4,6,7,8,9,10] #the order of the print and variable shouldn't matter
print x
def say_hello(name):
    if name: #identation is needed for every new block of code
        print "Hello,"+name+"from inside function"
    else:
        print "no name"
print "outside of function"
print "this is a sample string"
name  = "Zen"
print "My name is", name
print "My name is " + name
"""
this is concatenanting the contents into a new string but you need to add a sapce at the end of (is) otherwise it will just pring My name isname
"""
first_name = "Juile"
last_name = "Coder"
print "My name is {}{}".format(first_name, last_name)

#{} and the string (.format) method to inject variables into your string which is known as (string interpolation)
x = "hello World!"
print x.capitalize() #this would just capitalize the first letter of the string

ninjas = ["Frozen", "IceQueen", "Aslan"]
my_list = ["4", ["list", "in", "a", "list"], 987]#this is a list within a list
print ninjas + my_list #i am concatenanting
drawer = ["documents", "envelopes", "pens"]
print drawer [0]
print drawer [1]
print drawer [2]
#this is accessing values by referencing their index number

x = [1,2,3,4,5,6]
x.append(999)
print x
#this is adding a new number basically. appending is adding shit or MANIPULATING A list

x = [99, 100, 2, 4, 5, -4];
print x[:] #output would be [99,100,2,4,5, -4]
print x[1:] #output would be [100,2,3,5,-4]
print x[:4]#[99,100,2,4]
print x[2:4]#[2,5]

my_list = [1, "zen", "hi"]
print len(my_list) #this will print out the length of the array

age = 18 #these are conditionals, if and else statements.
if age >=21:
    print "drinking time"
else:
    print "yall are crazy"
age =100
if age >=50:
    print "YOU'RE GOING TO DIE SOON"
elif age==25:#if you have another condition you would use (elif)
    print "Midlife crisisisisisisisi"
else:
    print "you're close to dying"
for count in range (0, 10):#for loop but it only counts up to 9 since this acts like a for loop
    print "I'm counting ", count

two_list = [1, 2, 3, 4, "bog", "dog",["list", "within", "a", "list"], "hello world"]
for element in two_list:
    print element
#this is printg out all the elements in my two_list
hw = "Julie is My name %s" % "pupper"
print hw
# this is another way to concatenanting or adding new variables into a string

count = 1
while count < 10:
    print "im counting ", count
    count += 2
#this is making a while loops

for val in "string":
    if val =="i":
        break
    print(val)
#careful with indentation
#this is using (break) function to break out of a loop.

for val in "beautiful":
    if val == "e":
        continue
    print(val)
# as always continue will continue the loop after it completely skips over "e".

class EmptyClass:
    pass
my_string = [1,2,3,4,5]
for val in my_string:
    pass
    #this would just pass it, no code will be executed

x = 3
y = x
while y > 0:
    print y
    y = y - 1
else:
    print "final else statement"
    #it should print out 3,2,1 and then final else statement

x = 3
y = x
while y > 0:
    print y
    y = y - 1
    if y == 0:
        break
else:
    print "final else statement"
    #it broke out of the loop when y==0

my_string = "IT's Thanksgiving day. It's my birthday too!"
for val in my_string:
    if val == "day":
        break
    print my_string
