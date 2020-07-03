def rec_subset(toConsider, total, i):
    """Assumes toConsider is a list of items, total is sum of subset
       item values. Returns the number of subsets of toConsider that 
       add up to the total. i is the index that subsets being considered to.
       This is a case of the Brute Force Algorithm by recursive decision tree.
       """
    if total == 0:
        # zero total will have 1 empty subset {}
        result = 1
    elif total < 0:
        #negative total will return 0 number of subsets add up to it
        result = 0
    elif i < 0:
        result = 0
    elif toConsider[i] > total:
        #ith element eliminated, Explore the elements to the left of the list
        result = rec_subset(toConsider, total, i-1)
    else:
        result = rec_subset(toConsider, total-toConsider[i], i-1) + \
                    rec_subset(toConsider, total, i-1)
    return result

            
def count_sets(array, total):
    return rec_subset(array, total, len(array)-1)



def rec_dp(array, total, i, mem):
    """this is dynamic programming recursive subset function where
       an additional data structure mem to store dynamic intermediate result
    """
    # use string key to identify the mem 
    key = str(total) + ':' + str(i)
    if key in mem:
        return mem[key]
    if total == 0:
        # zero total will have 1 empty subset {}
        return 1
    elif total < 0:
        #negative total will return 0 number of subsets add up to it
        return 0
    elif i < 0:
        return 0
    elif array[i] > total:
        #ith element eliminated, Explore the elements to the left of the list
        to_return = rec_dp(array, total, i-1, mem)
    else:
        to_return = rec_dp(array, total-array[i], i-1, mem) + \
                    rec_dp(array, total, i-1, mem)
    # store to_return in mem[key] before returning it
    mem[key] = to_return
    return to_return
    
def count_dp(array, total):
    """dynamic programming count_sets function that returns addtional
       dict mem """
    mem = {} # empty dict or hash table
    return rec_dp(array, total, len(array)-1, mem)
   
def test_count(cows, total_weight, printItems = True):
    print('Use search tree to add up weight to', total_weight,
          'tons')
    #num = count_sets(cows, total_weight)
    num = count_dp(cows, total_weight)
    print('Total number of subsets taken =', num)

cows_list = [2, 4, 6, 10]
test_count(cows_list, 16)