result = True
count = 0
while result == True:
    if count <3:
        number = int(input())
        if number == 72:
            print("win")
            result = False
        else:
            print("again")
            count += 1
    else:
        print("lost")
        result = False