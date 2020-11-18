
def find_pairs(my_list, goal):
    for n in range(1,len(my_list)):
        if (my_list[n] + my_list[n - 1]) == goal:
            return True
    return False
        
    
res = find_pairs([1,2,3,9], 8)
assert res == False, res

res = find_pairs([1,2,4,4], 8)
assert res == True, res





