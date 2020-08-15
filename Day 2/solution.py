import numpy
def day2(arr):
    x = numpy.prod(arr)
    new_arr = []
    for i in range(0,len(arr)):
        j = x//arr[i] 
        new_arr.append(j)
    return new_arr

print(day2([3,2,1]))

# I love to know if you have any other good way to solve this problem 🙂