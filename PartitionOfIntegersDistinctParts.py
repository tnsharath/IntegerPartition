# numpy for better 2D array initialisation
import numpy as np

# print the sequence of partition of integer with distinct elements
def show_sequence(T):
    print("Sequence of partition of integer with distinct elements:")
    for i in range(0, len(T)):
        if i < len(T) - 1:
            print(T[i][i], end= ", ")
        else:
            print(T[i][i])

# Function to return the number of partition of integers with distinct combinations.
# Eg.1. n = 5
# Result = 3
# Eg.2. n = 8
# Result = 6
def distinct_partition(n):
    # perform operation till n + 1
    n = n + 1
    
    # initialize arrays with zero
    T = np.zeros((n, n))
    
    # converting float64 to int64
    T = T.astype(np.int64)
    
    # initialize T[0][0] to 1, 
    # base condition will be [1, 0, 0, 0, 0, .... 0(n)]
    T[0][0] = 1
    
    # loop through 2D - array, excluding base condition
    for i in range(1, n):
        for j in range(0, n):
            
            # j is the sum we are trying to achieve with {0-i} integers,
            if i > j:
                
                # copy immediate above value to current position
                T[i][j] = T[i - 1][j]
            else:
                
                # case 1. number of combination of making sum of j without ith integer,
                #         i.e T[i - 1][j]
                # case 2. number of combination of making sum of j with ith integer,
                #         i.e T[i - 1][j - i]
                T[i][j] = T[i - 1][j] + T[i - 1][j - i]
                
    # sequence. Comment the below line if sequence is not required.          
    show_sequence(T)
                
    # return the number of possible combination of distinct partition.
    return T[n - 1][n - 1]

# provide n
n = 8
print("Number of ways of Partition of integers with distinct parts: ", distinct_partition(n))




