"""
Different Codes For Recursions. 
"""

###################################################################################################
###################################################################################################

"""
This is a Draw Ruler Function.
"""

def draw_line(tick_length, tick_label=''):
    line = '-'*tick_length
    if tick_label:
        line+=' '+tick_label 
    print(line)

def draw_interval(center_length):
    if center_length>0:
        draw_interval(center_length-1)
        draw_line(center_length)
        draw_interval(center_length-1)

def draw_ruler(num_inches,major_length):
    draw_line(major_length,'0')
    for j in range(1,1+num_inches):
        draw_interval(major_length-1)
        draw_line(major_length,str(j))

# Uncomment The following line to run this function.
#draw_ruler(1,5)


###################################################################################################
###################################################################################################

"""
Binary Search: This works on sorted array only. So sort array before you feed to algorithm.
This is done in O(log n) time complexity.
"""

def binary_search(data, target, low, high):

    if low>high:
        return False
    else:
        mid = (low+high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data,target,mid+1, high)

# Uncomment Following lines to run function.
""" 
data = [21,78,78,98,76,4,3,2,5,6,7,353,645,34,22,79,90]
data.sort()
low = 0
high = len(data)-1
print(binary_search(data, 645, low, high)) 
"""

###################################################################################################
###################################################################################################

"""
Factorial Function.
"""
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

# Uncomment Following lines to run function.
""" 
i = int(input())
print(factorial(i)) 
"""

###################################################################################################
###################################################################################################

"""

"""