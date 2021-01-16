array = eval(input())
newArray = []
for key in array:
    if key["price"]<20:
        newArray.append(key["name"])

print(newArray)