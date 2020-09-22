# Count the number of items in a list, using recursion.

# For example:

# >>> count_recursively([])
# 0

# >>> count_recursively([1, 2, 3])
# 3


def length_of_list(lst):
    """Return number of items in a list, using recursion."""

    if not lst:
        #list_length = 0
        return 0  
            
    #list_length = 1 + length_of_list(lst[1:])

    return 1 + length_of_list([1:])

#Tests:
#lst = []
#list_length = 0 

#lst = [1,2,3]
#list_length = 1 + f[2,3]
#list_length = 1 + 1 + f[3]
#list_length = 1 + 1 + 1


