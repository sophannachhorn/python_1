array = eval(input())
reuslt = ""
number = 0
for i in range(len(array)):
    if len(array[i]) >=4 and len(array[i]) <=6:
        number += 1
if number == len(array):
    print("GOOD")
else:
    print("BAD")