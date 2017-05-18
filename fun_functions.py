#def evenstevens()
evenstevens = range(1,2001)
for x in evenstevens:
    if x % 2 == 0:
        print "number is", x, " this is an even number."
    else:
        print "number is", x, " this is an odd number."

#multiplying everything by 5
def mulitply_time(arr, num):
    for i in range(0,len(arr)):
        arr[i] *= num
    return arr
timeArray= [4,6,7,8,9]
print mulitply_time(timeArray, 5)

#Printing out all ones
def layerd_multiples(arr):
    print arr
    new_arry = []
    for x in arr:
        val_arr = []
        for i in range(0,x):
            val_arr.append(1)
        new_arry.append(val_arr)
    return new_arry
x = layerd_multiple([2,4,5],3))
print x
