class CanNotOrderAdjacentElements(Exception):
    pass

def is_consec(ordering, subset):
    if len(subset)==0:
        return True
    
    indexes = list(map(ordering.index, subset))
    diff = max(indexes)-min(indexes)
    return diff==len(subset)-1
    
def check_order(connecteds, ordering):
    return all([is_consec(ordering,cc) for cc in connecteds])

def get_order(connecteds):
    from itertools import permutations
    from functools import reduce
    alphabet = reduce(set.union, connecteds, set())
    for order in permutations(alphabet):
        if check_order(connecteds,order):
            return order
    #Otherwise:
    raise(CanNotOrderAdjacentElementsError())
    