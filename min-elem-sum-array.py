'''
Python program to find minimum elements in array which has sum equals to given value. Input Array : [10, 0, -1, 20, 25, 30] Required Sum: 45 Output: [20, 25] Required Sum: 29 Output: [-1, 30]
'''

import itertools


def findelem(sum, array):
    for i in range(1, len(array) + 1):
        for tpl in itertools.combinations(array, i):
            lenoftuple = len(tpl)
            cursum = tpl[0]
            if cursum == sum:
                return tpl[0]
            else:
                for j in range(1, lenoftuple):
                    cursum += tpl[j]
                if cursum == sum:
                    return list(tpl)


sum1 = 45
sum2 = 29
array = [10, 0, -1, 20, 25, 30]
print('Input Array: ', array,
      '\nRequired Sum: ', sum1,
      '\nOutput: ', findelem(sum1, array))
print('Input Array: ', array,
      '\nRequired Sum: ', sum2,
      '\nOutput: ', findelem(sum2, array))

'''
Outputs:

Input Array:  [10, 0, -1, 20, 25, 30] 
Required Sum:  45 
Output:  [20, 25]
Input Array:  [10, 0, -1, 20, 25, 30] 
Required Sum:  29 
Output:  [-1, 30]
'''
