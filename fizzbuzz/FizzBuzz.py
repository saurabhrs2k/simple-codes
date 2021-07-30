c3 = 0
c5 = 0
for x in range(1,101):
    c3+=1
    c5+=1
    output = ""
    if(c3 == 3):
        output += 'Fizz'
        c3 = 0
    if(c5 == 5):
        output += 'Buzz'
        c5 = 0
    if(output == ""):
        output += str(x)
    print(output)
