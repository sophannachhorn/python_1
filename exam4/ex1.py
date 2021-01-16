array = eval(input())
indexOfseven = 0
isFound = 0
for i in range(len(array)):
    if isFound <1:
        if array[i] == 7:
            indexOfseven = i
            isFound +=1     
if isFound == 1:
        print("The first 7 is at index",indexOfseven)
else:
        print("Not found")
