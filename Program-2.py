#  Problem-2: With a single integer as the input, generate the following until
#  a = x [series of numbers as shown in below examples]
#     Output: (examples)
#         1) input a = 1, then output : 1
#         2) input a = 2, then output : 1, 3
#         3) input a = 3, then output : 1, 3, 5
#         4) input a = 4, then output : 1, 3, 5, 7
#         .
#         X) input a = x, then output : 1, 3, 5, 7, .......

no_of_outputs=5
value_printed=1

for i in range(no_of_outputs):
    print(value_printed,end=" ")
    value_printed = value_printed + 2

#OUTPUT =  1 3 5 7 9 