array=eval(input())
indexOfseven = 0
result = True

for i in range(len(array)):
    if array[i] == 7:
        indexOfseven = i
        result = False
if result == False:
    print("The first 7 is at index",indexOfseven)
else:
    print("Not found")
