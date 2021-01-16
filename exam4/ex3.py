array = eval(input())
indexOfseven = []
result = False
for i in range(len(array)):
   
    if array[i] == 7:
        indexOfseven.append(i)
        result = True
if result == True:
    print("7 found at indexes:",indexOfseven)
else:
    print("Not found")


