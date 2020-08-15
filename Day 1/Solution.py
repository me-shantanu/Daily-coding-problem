from itertools import combinations 
def day1(arr,k):
    comb = combinations(arr,2)
    for i in list(comb):
        if sum(list(i)) == k:
            print("True")
            break

day1([10, 15, 3, 7],17)


# I love to know if you have any other good way to solve this problem 🙂