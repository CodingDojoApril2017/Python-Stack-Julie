#series of stars in a checkerboard pattern
for x in range(8):
    myStr = ''
    if x % 2 == 1:
        myStr += ' '
    for y in range(4):
        myStr += '* '
    print myStr

for x in range(8):
    myStr = ''
    if x % 2 == 1:
        myStr += ' '

    myStr += '* ' * 4

    print myStr
