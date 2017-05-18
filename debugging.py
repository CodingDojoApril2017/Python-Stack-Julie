
#print "hello julie"
"""
def multiply(arr,num):
    print arr, num
    for x in arr:
        x *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b
"""
#tuple_data = ('physics', 'chemistry', 'x-ray', 'x-sby')
#tuple_num = (67, 89, 31, 15)
#print max(tuple_data)
#print max(tuple_num)

#tuple_num =(67, 89, 31, 2, 1, 1, 2)#(0, False, '', 0.0, []) (67, 89, 31, False, 0, None, [])
#print all(tuple_num)

num = (1, 5, 7, 3, 8)
for index, item in enumerate(num):
    print(str(index)+""+str(item))

num = (1, 5, 7, 3, 8)
print sorted(num)

weekend = {"Sun": "Sunday", "Mon": "Monday"} #literal notation
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"

data ={"house":"Haus","cat":"Katze","red":"rot"}
print data.items()
#[('house', 'Haus'), ('red', 'rot'), ('cat', 'Katze')]
print data.keys()
#['house', 'red', 'cat']
print data.values()
#['Haus', 'rot', 'Katze']

def get_odds():
    for i in range (1,2000):
        if i%2 == 0:
            print i + "this is an even number"
        else:
            print i + "this is an odd number"
get_odds(1,2000)
