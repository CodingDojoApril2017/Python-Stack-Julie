
my_list= ["potato","thats a long sentence", ['name','address','phone number','social security number'] ,10, 12, 100, 40, 200]
def filter_by_type(my_list):
    #my_list = [150]
    for x in my_list:
        if type(x) == int:
            if x >=100:
                print "thats a big number!"
            else:
                print "thats a small number!"
        if type(x) == str:
            if x >=50:
                print "thats a long sentece"
            else:
                print "that's a short one"
        if type(x) == list:
            if x >= 10:
                print "long list"
            else:
                print "short list"
filter_by_type(my_list)
