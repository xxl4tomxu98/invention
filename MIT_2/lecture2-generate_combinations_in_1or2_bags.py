# generate all combinations of N items
def powerSet(items):
    """For the following problem, consider the following way to write
       a power set generator. The number of possible combinations to
       put n items into one bag is  2**n . Here, items is a Python list.
       With one bag we determined there were  2**n  possible combinations
       available by representing the bag as a list of binary bits, 0 or 1.
       Since there are N bits, and they can be one of two possibilities,
       there must be  2**n  possibilities.
    """
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

#print(powerSet([1,3,4,7,9]))

def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list
        of which item(s) are in each bag.

        With two bags there thus must be  3**n  possible combinations.
        You can imagine this by representing the two bags as a list of
        "trinary" bits, 0, 1, or 2 (a 0 if an item is in neither bag;
        1 if it is in bag1; 2 if it is in bag2). With the "trinary" bits,
        there are N bits that can each be one of three possibilities
        - thus there must be  3**n  possible combinations.
    """
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in range(3**N):
        combo1 = []
        combo2 = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 3 == 1:
                combo1.append(items[j])
            elif (i >> j) % 3 == 2:
                combo2.append(items[j])
        yield (combo1, combo2)
print(yieldAllCombos([1,3,4,7,9]))
