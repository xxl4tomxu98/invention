#From codereview.stackexchange.com                    
def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b


# This is a helper function that will fetch all of the available 
# partitions for you to use for your brute force algorithm.
def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]

### Uncomment the following code  and run this file
### to see what get_partitions does if you want to visualize it:

# for item in (get_partitions(['a','b','c','d'])):
#     print(item)
        
def brute_force_cow_transport(cows, max_weights):  
    candidates = []     
    for trips in (get_partitions(cows.keys())):
        for trip in trips:
            if sum([cows[cow] for cow in trip]) > max_weights:
                trips = None
        if trips != None:
            candidates.append(trips)
    min_trip_num = min(len(i) for i in candidates)
    for i in candidates:
        if len(i) == min_trip_num:
            print(i)
cows = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5} 
brute_force_cow_transport(cows, 10)

