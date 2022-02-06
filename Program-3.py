'''Problem-3: With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]
    Output: (examples)
        1) input a = 1, then output : 1
        2) input a = 2, then output : 1
        3) input a = 3, then output : 1, 3, 5
        4) input a = 4, then output : 1, 3, 5
        5) input a = 5, then output : 1, 3, 5, 7, 9
        6) input a = 6, then output : 1, 3, 5, 7, 9
        .
        .
        X) input a = x, then output : 1, 3, 5, 7, .......'''

no_of_outputs=6   # FOR INPUT = 6
value_printed=1
if no_of_outputs % 2 == 0:
    no_of_outputs = no_of_outputs -1

for i in range(no_of_outputs):
    print(value_printed,end=" ")
    value_printed = value_printed + 2


#OUTPUT = 1 3 5 7 9 