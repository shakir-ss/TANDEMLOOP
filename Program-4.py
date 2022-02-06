
# Problem-4: Get the total count of number list in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]

# (examples)


# Output:
# {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}

input = [1,2,8,9,12,46,76,82,15,20,30]
dictn = dict()
count = 0
for i in range(1,10):
    for j in input:
        if j % i == 0:
            count = count + 1

    dictn.update({i:count})
    count = 0
print(dictn)

#OUTPUT ={1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}